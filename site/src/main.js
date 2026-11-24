import "./style.css";
import { mountCyberGlobe } from "./globe.js";

const globeStage = document.querySelector("#globe-stage");
const rotationToggle = document.querySelector("[data-rotation-toggle]");
const rotationLabel = document.querySelector("[data-rotation-label]");
const banner = document.querySelector("[data-banner]");
const bannerStatus = document.querySelector("[data-banner-status]");
const menuToggle = document.querySelector(".menu-toggle");
const navigation = document.querySelector(".main-nav");

const globe = mountCyberGlobe(globeStage);

if (rotationToggle && rotationLabel) {
  const initialRotation = globe?.getAutoRotate() ?? false;

  const updateRotationControl = (enabled) => {
    rotationToggle.setAttribute("aria-pressed", String(enabled));
    rotationLabel.textContent = enabled ? "AUTO ROTATE ON" : "AUTO ROTATE OFF";
  };

  updateRotationControl(initialRotation);

  rotationToggle.addEventListener("click", () => {
    if (!globe) return;
    const nextState = !globe.getAutoRotate();
    const actualState = globe.setAutoRotate(nextState);
    updateRotationControl(actualState);
  });
}

if (banner && bannerStatus) {
  banner.addEventListener("error", () => {
    bannerStatus.hidden = false;
    banner.closest(".hero-banner")?.classList.add("banner-artwork-missing");
  }, { once: true });

  banner.addEventListener("load", () => {
    bannerStatus.hidden = true;
    banner.closest(".hero-banner")?.classList.remove("banner-artwork-missing");
  }, { once: true });
}

if (menuToggle && navigation) {
  menuToggle.addEventListener("click", () => {
    const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isOpen));
    navigation.classList.toggle("nav-open", !isOpen);
  });

  navigation.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navigation.classList.remove("nav-open");
      menuToggle.setAttribute("aria-expanded", "false");
    });
  });
}

const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
if (reducedMotion.matches) {
  document.documentElement.classList.add("reduced-motion");
}

reducedMotion.addEventListener?.("change", (event) => {
  document.documentElement.classList.toggle("reduced-motion", event.matches);
});

window.addEventListener("pagehide", () => globe?.dispose(), { once: true });
