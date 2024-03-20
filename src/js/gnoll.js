import gwFactory from './gnollwasm.js';

//var Module = null; const modulePromise = await gwFactory().then(x => Module = x);

/*
export function roll(notation) {
  Module.resetOut();

  Module.cwrap('roll_full_options', 'number', ['string',
      'string', 'number', 'number', 'number', 'number', 'number',
      'number'],
    [notation, null, 0, 0, 0, 1, 0, 0]
  );

  return Module.stdout;
}
*/
export async function roll(notation) {
  return new Promise((resolve) => {
    gwFactory().then((Module) => {
      Module.resetOut();

      Module.ccall('roll_full_options', 'number', ['string',
          'string', 'number', 'number', 'number', 'number', 'number',
          'number'],
        [notation, null, 0, 0, 0, 1, 0, 0]
      );

      resolve( Module.stdout );
  });

  });
}

export function temproll(notation) {
  return "foobar";
}
