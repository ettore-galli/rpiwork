import { render, screen } from '@testing-library/react';
import inductance from './Solenoid';

test('inductance gives a value', () => {
  expect(inductance(1, 1, 1, 1)).toBeCloseTo(9.86931332662495e-7, 3);
});
