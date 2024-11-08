import React, { useState, useEffect } from 'react';
import { Button, Label } from '@/components';
import { Plus, Minus } from 'lucide-react';

const Timer = () => {
  const [hours, setHours] = useState(0);
  const [minutes, setMinutes] = useState(0);
  const [seconds, setSeconds] = useState(0);
  const [isRunning, setIsRunning] = useState(false);
  const [lapTimes, setLapTimes] = useState([]);

  useEffect(() => {
    let intervalId;
    if (isRunning) {
      intervalId = setInterval(() => {
        if (seconds === 59) {
          setSeconds(0);
          if (minutes === 59) {
            setMinutes(0);
            setHours(hours + 1);
          } else {
            setMinutes(minutes + 1);
          }
        } else {
          setSeconds(seconds + 1);
        }
      }, 1000);
    }
    return () => clearInterval(intervalId);
  }, [isRunning, hours, minutes, seconds]);

  const handleStartPause = () => {
    setIsRunning(!isRunning);
  };

  const handleReset = () => {
    setIsRunning(false);
    setHours(0);
    setMinutes(0);
    setSeconds(0);
    setLapTimes([]);
  };

  const handleLap = () => {
    setLapTimes([...lapTimes, `${hours}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`]);
  };

  const handleAddMinutes = (amount) => {
    setMinutes(minutes + amount);
  };

  return (
    <div className="max-w-md mx-auto p-4">
      <div className="flex justify-center mb-4">
        <Label className="text-6xl">
          {hours}:{minutes.toString().padStart(2, '0')}:{seconds.toString().padStart(2, '0')}
        </Label>
      </div>
      <div className="flex justify-center mb-4">
        <Button onClick={() => handleAddMinutes(5)} className="mr-2">
          <Plus size={24} />
          Add 5 minutes
        </Button>
        <Button onClick={() => handleAddMinutes(-5)} className="mr-2">
          <Minus size={24} />
          Remove 5 minutes
        </Button>
      </div>
      <div className="flex justify-center mb-4">
        <Button onClick={handleStartPause} className="mr-2">
          {isRunning ? 'Pause' : 'Start'}
        </Button>
        <Button onClick={handleReset} className="mr-2">
          Reset
        </Button>
        <Button onClick={handleLap}>
          Lap
        </Button>
      </div>
      <div className="flex justify-center mb-4">
        <ul>
          {lapTimes.map((lapTime, index) => (
            <li key={index}>{lapTime}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Timer;