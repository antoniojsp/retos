
const isValid = require('./your_file'); // Assuming your code is in your_file.js

describe('isValid', () => {
  it('should return true for an empty string', () => {
    expect(isValid('')).toBe(true);
  });

  it('should return true for a valid parenthesis string', () => {
    expect(isValid('()')).toBe(true);
    expect(isValid('()[]{}')).toBe(true);
    expect(isValid('{[]}')).toBe(true);
    expect(isValid('([{}])')).toBe(true);
  });

  it('should return false for an invalid parenthesis string', () => {
    expect(isValid('(]')).toBe(false);
    expect(isValid('([)]')).toBe(false);
    expect(isValid('((')).toBe(false);
    expect(isValid('{{}[][[[]])]')).toBe(false);
  });

  it('should return false for a string with only opening parenthesis', () => {
    expect(isValid('((')).toBe(false);
    expect(isValid('[{')).toBe(false);
  });

  it('should return false for a string with only closing parenthesis', () => {
    expect(isValid(')')).toBe(false);
    expect(isValid('}])')).toBe(false);
  });
});