#!/usr/bin/env node
/**
 * Reproducible entry point for the Brooklyn Nine-Nine README Earth banner.
 * Requires Python 3 and the packages listed in requirements-render.txt.
 */
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const renderer = path.join(here, 'render_header.py');
const python = process.env.PYTHON ?? 'python3';
const result = spawnSync(python, [renderer, ...process.argv.slice(2)], { stdio: 'inherit' });
if (result.error) {
  console.error('Unable to start Python renderer: ' + result.error.message);
  process.exit(1);
}
process.exit(result.status ?? 1);
