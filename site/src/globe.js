import * as THREE from "three";
import ThreeGlobe from "three-globe";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const COLORS = {
  yellow: "#f5d90a",
  green: "#39ff88",
  red: "#ff5f56",
  cyan: "#63d7ff"
};

// Synthetic coordinates for visual demonstration only.
// These arcs do not describe real traffic, attacks, or infrastructure.
const DEMO_NODES = [
  { name: "NEW YORK", lat: 40.7128, lng: -74.006, color: COLORS.yellow },
  { name: "LONDON", lat: 51.5072, lng: -0.1276, color: COLORS.green },
  { name: "SAO PAULO", lat: -23.5505, lng: -46.6333, color: COLORS.cyan },
  { name: "TOKYO", lat: 35.6762, lng: 139.6503, color: COLORS.red },
  { name: "BERLIN", lat: 52.52, lng: 13.405, color: COLORS.yellow },
  { name: "SINGAPORE", lat: 1.3521, lng: 103.8198, color: COLORS.green },
  { name: "SYDNEY", lat: -33.8688, lng: 151.2093, color: COLORS.cyan }
];

const DEMO_ARCS = [
  { startLat: 40.7128, startLng: -74.006, endLat: 51.5072, endLng: -0.1276, color: COLORS.green },
  { startLat: 40.7128, startLng: -74.006, endLat: -23.5505, endLng: -46.6333, color: COLORS.yellow },
  { startLat: 51.5072, startLng: -0.1276, endLat: 35.6762, endLng: 139.6503, color: COLORS.cyan },
  { startLat: 52.52, startLng: 13.405, endLat: 1.3521, endLng: 103.8198, color: COLORS.green },
  { startLat: 1.3521, startLng: 103.8198, endLat: -33.8688, endLng: 151.2093, color: COLORS.yellow },
  { startLat: 35.6762, startLng: 139.6503, endLat: 40.7128, endLng: -74.006, color: COLORS.red }
];

function createStarField() {
  const count = 900;
  const positions = new Float32Array(count * 3);

  for (let index = 0; index < count; index += 1) {
    const radius = 310 + Math.random() * 230;
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(2 * Math.random() - 1);
    positions[index * 3] = radius * Math.sin(phi) * Math.cos(theta);
    positions[index * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
    positions[index * 3 + 2] = radius * Math.cos(phi);
  }

  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));

  const material = new THREE.PointsMaterial({
    color: "#9ac6ad",
    size: 0.9,
    transparent: true,
    opacity: 0.48,
    sizeAttenuation: true,
    depthWrite: false
  });

  return new THREE.Points(geometry, material);
}

function disposeObject(root) {
  root.traverse((object) => {
    if (object.geometry) object.geometry.dispose();

    if (object.material) {
      const materials = Array.isArray(object.material) ? object.material : [object.material];
      materials.forEach((material) => {
        for (const value of Object.values(material)) {
          if (value && value.isTexture) value.dispose();
        }
        material.dispose();
      });
    }
  });
}

export function mountCyberGlobe(container) {
  if (!container) return null;

  const fallback = container.querySelector("[data-globe-fallback]");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({
      alpha: true,
      antialias: true,
      powerPreference: "high-performance"
    });
  } catch (error) {
    if (fallback) {
      fallback.hidden = false;
      fallback.querySelector("strong").textContent = "3D VIEW UNAVAILABLE";
      fallback.querySelector("small").textContent = "WebGL is unavailable in this browser or device.";
    }
    return null;
  }

  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.8));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.15;
  renderer.domElement.className = "globe-renderer";
  renderer.domElement.setAttribute("aria-label", "Interactive 3D globe with illustrative network arcs");
  container.appendChild(renderer.domElement);
  if (fallback) fallback.hidden = true;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(36, 1, 0.1, 1200);
  camera.position.set(0, 0, 285);

  scene.add(new THREE.AmbientLight("#8cae9c", 1.4));

  const keyLight = new THREE.PointLight("#b5ffd4", 95, 650, 1.7);
  keyLight.position.set(-160, 110, 180);
  scene.add(keyLight);

  const rimLight = new THREE.PointLight(COLORS.yellow, 50, 500, 2);
  rimLight.position.set(140, -80, -120);
  scene.add(rimLight);

  const globe = new ThreeGlobe()
    .globeImageUrl("https://unpkg.com/three-globe/example/img/earth-dark.jpg")
    .bumpImageUrl("https://unpkg.com/three-globe/example/img/earth-topology.png")
    .showAtmosphere(true)
    .atmosphereColor(COLORS.green)
    .atmosphereAltitude(0.18)
    .showGraticules(true)
    .arcsData(DEMO_ARCS)
    .arcColor((datum) => datum.color)
    .arcStroke(0.52)
    .arcAltitudeAutoScale(0.34)
    .arcDashLength(0.42)
    .arcDashGap(0.22)
    .arcDashInitialGap(() => Math.random() * 0.7)
    .arcDashAnimateTime(2600)
    .pointsData(DEMO_NODES)
    .pointColor((datum) => datum.color)
    .pointAltitude(0.025)
    .pointRadius(0.46)
    .ringsData(DEMO_NODES)
    .ringColor((datum) => datum.color)
    .ringMaxRadius(2.15)
    .ringPropagationSpeed(0.75)
    .ringRepeatPeriod(1450);

  globe.rotation.y = -0.35;
  scene.add(globe);

  const starField = createStarField();
  scene.add(starField);

  const orbitMaterial = new THREE.MeshBasicMaterial({
    color: COLORS.green,
    transparent: true,
    opacity: 0.16,
    side: THREE.DoubleSide,
    depthWrite: false
  });
  const orbit = new THREE.Mesh(
    new THREE.TorusGeometry(106, 0.12, 4, 180),
    orbitMaterial
  );
  orbit.rotation.x = THREE.MathUtils.degToRad(72);
  orbit.rotation.y = THREE.MathUtils.degToRad(-18);
  scene.add(orbit);

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.045;
  controls.enablePan = false;
  controls.enableZoom = false;
  controls.rotateSpeed = 0.42;
  controls.minPolarAngle = Math.PI * 0.24;
  controls.maxPolarAngle = Math.PI * 0.76;
  controls.target.set(0, 0, 0);

  let width = 0;
  let height = 0;
  let animationFrame = 0;
  let autoRotate = !reducedMotion;
  let visible = true;
  let disposed = false;

  const resize = () => {
    const bounds = container.getBoundingClientRect();
    width = Math.max(1, Math.floor(bounds.width));
    height = Math.max(1, Math.floor(bounds.height));
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  };

  const resizeObserver = new ResizeObserver(resize);
  resizeObserver.observe(container);
  resize();

  const stopLoop = () => {
    if (animationFrame) {
      cancelAnimationFrame(animationFrame);
      animationFrame = 0;
    }
  };

  const visibilityObserver = new IntersectionObserver(([entry]) => {
    visible = entry.isIntersecting;
    if (visible) startLoop();
    else stopLoop();
  }, { threshold: 0.04 });
  visibilityObserver.observe(container);

  const onVisibilityChange = () => {
    if (document.hidden) stopLoop();
    else startLoop();
  };
  document.addEventListener("visibilitychange", onVisibilityChange);

  const clock = new THREE.Clock();

  const renderFrame = () => {
    animationFrame = 0;
    if (disposed || !visible || document.hidden) return;

    const delta = Math.min(clock.getDelta(), 0.05);
    if (autoRotate) {
      globe.rotation.y += delta * 0.055;
      orbit.rotation.z += delta * 0.018;
      starField.rotation.y += delta * 0.003;
    }

    controls.update();
    renderer.render(scene, camera);
    animationFrame = requestAnimationFrame(renderFrame);
  };

  const startLoop = () => {
    if (!animationFrame && visible && !document.hidden && !disposed) {
      clock.start();
      animationFrame = requestAnimationFrame(renderFrame);
    }
  };

  startLoop();

  return {
    setAutoRotate(enabled) {
      autoRotate = Boolean(enabled) && !reducedMotion;
      return autoRotate;
    },
    getAutoRotate() {
      return autoRotate;
    },
    dispose() {
      disposed = true;
      stopLoop();
      resizeObserver.disconnect();
      visibilityObserver.disconnect();
      document.removeEventListener("visibilitychange", onVisibilityChange);
      controls.dispose();
      disposeObject(scene);
      renderer.dispose();
      renderer.domElement.remove();
    }
  };
}
