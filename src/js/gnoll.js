import gwFactory from './gnollwasm.js';

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

