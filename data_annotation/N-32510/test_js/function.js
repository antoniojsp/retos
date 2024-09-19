
 function _generateKeyPair(state, options, callback) {
    if(typeof options === 'function') {
      callback = options;
      options = {};
    }
  
    // web workers unavailable, use setImmediate
    if(false || typeof(Worker) === 'undefined') {
      function step() {
        // 10 ms gives 5ms of leeway for other calculations before dropping
        // below 60fps (1000/60 == 16.67), but in reality, the number will
        // likely be higher due to an 'atomic' big int modPow
        if(forge.pki.rsa.stepKeyPairGenerationState(state, 10)) {
          return callback(null, state.keys);
        }
        forge.util.setImmediate(step);
      }
      return step();
    }
  
    // use web workers to generate keys
    var numWorkers = options.workers || 2;
    var workLoad = options.workLoad || 100;
    var range = workLoad * 30/8;
    var workerScript = options.workerScript || 'forge/prime.worker.js';
    var THIRTY = new BigInteger(null);
    THIRTY.fromInt(30);
    var op_or = function(x,y) { return x|y; };
    generate();
  
    function generate() {
      // find p and then q (done in series to simplify setting worker number)
      getPrime(state.pBits, function(err, num) {
        if(err) {
          return callback(err);
        }
        state.p = num;
        getPrime(state.qBits, finish);
      });
    }
  
    // implement prime number generation using web workers
    function getPrime(bits, callback) {
      // TODO: consider optimizing by starting workers outside getPrime() ...
      // note that in order to clean up they will have to be made internally
      // asynchronous which may actually be slower
  
      // start workers immediately
      var workers = [];
      for(var i = 0; i < numWorkers; ++i) {
        // FIXME: fix path or use blob URLs
        workers[i] = new Worker(workerScript);
      }
      var running = numWorkers;
  
      // initialize random number
      var num = generateRandom();
  
      // listen for requests from workers and assign ranges to find prime
      for(var i = 0; i < numWorkers; ++i) {
        workers[i].addEventListener('message', workerMessage);
      }
  
      /* Note: The distribution of random numbers is unknown. Therefore, each
      web worker is continuously allocated a range of numbers to check for a
      random number until one is found.
  
      Every 30 numbers will be checked just 8 times, because prime numbers
      have the form:
  
      30k+i, for i < 30 and gcd(30, i)=1 (there are 8 values of i for this)
  
      Therefore, if we want a web worker to run N checks before asking for
      a new range of numbers, each range must contain N*30/8 numbers.
  
      For 100 checks (workLoad), this is a range of 375. */
  
      function generateRandom() {
        var bits1 = bits - 1;
        var num = new BigInteger(bits, state.rng);
        // force MSB set
        if(!num.testBit(bits1)) {
          num.bitwiseTo(BigInteger.ONE.shiftLeft(bits1), op_or, num);
        }
        // align number on 30k+1 boundary
        num.dAddOffset(31 - num.mod(THIRTY).byteValue(), 0);
        return num;
      }
  
      var found = false;
      function workerMessage(e) {
        // ignore message, prime already found
        if(found) {
          return;
        }
  
        --running;
        var data = e.data;
        if(data.found) {
          // terminate all workers
          for(var i = 0; i < workers.length; ++i) {
            workers[i].terminate();
          }
          found = true;
          return callback(null, new BigInteger(data.prime, 16));
        }
  
        // overflow, regenerate prime
        if(num.bitLength() > bits) {
          num = generateRandom();
        }
  
        // assign new range to check
        var hex = num.toString(16);
  
        // start prime search
        e.target.postMessage({
          e: state.eInt,
          hex: hex,
          workLoad: workLoad
        });
  
        num.dAddOffset(range, 0);
      }
    }
  
    function finish(err, num) {
      // set q
      state.q = num;
  
      // ensure p is larger than q (swap them if not)
      if(state.p.compareTo(state.q) < 0) {
        var tmp = state.p;
        state.p = state.q;
        state.q = tmp;
      }
  
      // compute phi: (p - 1)(q - 1) (Euler's totient function)
      state.p1 = state.p.subtract(BigInteger.ONE);
      state.q1 = state.q.subtract(BigInteger.ONE);
      state.phi = state.p1.multiply(state.q1);
  
      // ensure e and phi are coprime
      if(state.phi.gcd(state.e).compareTo(BigInteger.ONE) !== 0) {
        // phi and e aren't coprime, so generate a new p and q
        state.p = state.q = null;
        generate();
        return;
      }
  
      // create n, ensure n is has the right number of bits
      state.n = state.p.multiply(state.q);
      if(state.n.bitLength() !== state.bits) {
        // failed, get new q
        state.q = null;
        getPrime(state.qBits, finish);
        return;
      }
  
      // set keys
      var d = state.e.modInverse(state.phi);
      state.keys = {
        privateKey: forge.pki.rsa.setPrivateKey(
          state.n, state.e, d, state.p, state.q,
          d.mod(state.p1), d.mod(state.q1),
          state.q.modInverse(state.p)),
        publicKey: forge.pki.rsa.setPublicKey(state.n, state.e)
      };
  
      callback(null, state.keys);
    }
  }
  
  /**
   * pki.rsa.generateKeyPair
   */
  
  pki.rsa.generateKeyPair = function(bits, e, options, callback) {
    // (bits), (options), (callback)
    if(arguments.length === 1) {
      if(typeof bits === 'object') {
        options = bits;
        bits = undefined;
      }
      else if(typeof bits === 'function') {
        callback = bits;
        bits = undefined;
      }
    }
    // (bits, options), (bits, callback), (options, callback)
    else if(arguments.length === 2) {
      if(typeof bits === 'number') {
        if(typeof e === 'function') {
          callback = e;
        }
        else {
          options = e;
        }
      }
      else {
        options = bits;
        callback = e;
        bits = undefined;
      }
      e = undefined;
    }
