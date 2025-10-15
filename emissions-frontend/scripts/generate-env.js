const { writeFileSync } = require('fs');
const dotenv = require('dotenv');
const path = require('path');

const env = process.env.NODE_ENV || 'development';
const envFile = `.env.${env}`;
console.log(`Using environment file: ${envFile}`);

dotenv.config({ path: path.resolve(__dirname, `../${envFile}`) });

const targetPath = path.join(__dirname, '../src/environments/environment.ts');

const envConfigFile = `export const environment = {
  production: ${env === 'production'},
  apiUrl: '${process.env.API_URL}',
  defaultCountry: '${process.env.DEFAULT_COUNTRY}',
  defaultActivity: '${process.env.DEFAULT_ACTIVITY}',
  defaultEmissionType: '${process.env.DEFAULT_EMISSION_TYPE}'
};
`;

writeFileSync(targetPath, envConfigFile);
console.log(`Environment file generated for ${env}`);
console.log(`Environment file generated at ${targetPath}`);
console.log(`Scripts generate-env.js executed`);

