// vite.config.js
import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import tailwindcss from "@tailwindcss/vite"

export default defineConfig({
    plugins: [react(), tailwindcss()],
    server: {
        port: 5173,
        proxy: { "/api": "http://localhost:8000" },
    },
    build: {
        outDir: "dist",
        assetsDir: "assets",
        manifest: true,
        emptyOutDir: true,
    },
  base: "./",   // 👈 esta es la clave
})
