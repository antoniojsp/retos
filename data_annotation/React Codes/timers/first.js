import React, { useState, useEffect } from 'react';
import { Button, Label } from '@/components';
import { Plus, Minus } from 'lucide-react';

const Timer = () => {
  const [hours, setHours] = useState(0);
  const [minutes, setMinutes] = useState(0);
  const [seconds, setSeconds] = useState(0);
  const [isRunning, setIsRunning] = useState(false);
  const [laps, setLaps] = useState([]);
  const [intervalId, setIntervalId] = useState(null);

  useEffect(() => {
    if (isRunning) {
      const interval = setInterval(() => {
        if (seconds < 59) {
          setSeconds(seconds + 1);
        } else if (minutes < 59) {
          setMinutes(minutes + 1);
          setSeconds(0);
        } else {
          setHours(hours + 1);
          setMinutes(0);
          setSeconds(0);
        }
      }, 1000);
      setIntervalId(interval);
    } else if (intervalId) {
      clearInterval(intervalId);
    }
    return () => {
      clearInterval(intervalId);
    };
  }, [isRunning, seconds, minutes, hours]);

  const handleStart = () => {
    setIsRunning(true);
  };

  const handlePause = () => {
    setIsRunning(false);
  };

  const handleReset = () => {
    setIsRunning(false);
    setHours(0);
    setMinutes(0);
    setSeconds(0);
    setLaps([]);
  };

  const handleLap = () => {
    setLaps([...laps, `${hours}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`]);
  };

  const handleAddMinutes = () => {
    setMinutes(minutes + 1);
  };

  const handleRemoveMinutes = () => {
    if (minutes > 0) {
      setMinutes(minutes - 1);
    }
  };

  return (
    <div className="max-w-md mx-auto p-4">
      <div className="flex justify-center mb-4">
        <Label className="text-3xl">{hours.toString().padStart(2, '0')}:{minutes.toString().padStart(2, '0')}:{seconds.toString().padStart(2, '0')}</Label>
      </div>
      <div className="flex justify-center mb-4">
        <Button variant="outline" onClick={handleAddMinutes} className="mr-2">
          <Plus size={18} />
        </Button>
        <Button variant="outline" onClick={handleRemoveMinutes}>
          <Minus size={18} />
        </Button>
      </div>
      <div className="flex justify-center mb-4">
        <Button variant="default" onClick={handleStart} className="mr-2">Start</Button>
        <Button variant="default" onClick={handlePause} className="mr-2">Pause</Button>
        <Button variant="destructive" onClick={handleReset} className="mr-2">Reset</Button>
        <Button variant="default" onClick={handleLap}>Lap</Button>
      </div>
      <div className="flex flex-col justify-center">
        {laps.map((lap, index) => (
          <Label key={index} className="text-lg mb-2">Lap {index + 1}: {lap}</Label>
        ))}
      </div>
    </div>
  );
};

export default Timer;