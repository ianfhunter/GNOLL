import { Module } from '../../build/jsweb/out.js'

var roll_full_options = null;

Module.onRuntimeInitialized = _ => {
  roll_full_options = Module.cwrap('roll_full_options', 'number', ['string',
    'string', 'number', 'number', 'number', 'number', 'number',
    'number']);
};

export function roll(notation) {
  Module.resetOut();
  roll_full_options(notation, null, 0, 0, 0, 1, 0, 0);

  return Module.stdout;
}
