import { defineConfig } from "vite";

const repositoryBase = "/tryhackme-brooklyn-nine-nine/";

export default defineConfig({
  // Set GITHUB_PAGES=true in the Pages workflow to use the repository subpath.
  base: process.env.GITHUB_PAGES === "true" ? repositoryBase : "/",
  publicDir: "../assets",
  server: {
    host: "0.0.0.0",
    port: 5173,
    strictPort: true
  },
  preview: {
    host: "0.0.0.0"
  },
  build: {
    outDir: "dist",
    emptyOutDir: true,
    sourcemap: false
  }
});
