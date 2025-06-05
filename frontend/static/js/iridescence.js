 import { Renderer, Program, Mesh, Color, Triangle } from 'https://cdn.skypack.dev/ogl';

    const vertexShader = `
      attribute vec2 uv;
      attribute vec2 position;
      varying vec2 vUv;
      void main() {
        vUv = uv;
        gl_Position = vec4(position, 0, 1);
      }
    `;

    const fragmentShader = `
      precision highp float;
      uniform float uTime;
      uniform vec3 uColor;
      uniform vec3 uResolution;
      uniform vec2 uMouse;
      uniform float uAmplitude;
      uniform float uSpeed;
      varying vec2 vUv;
      void main() {
        float mr = min(uResolution.x, uResolution.y);
        vec2 uv = (vUv.xy * 2.0 - 1.0) * uResolution.xy / mr;
        uv += (uMouse - vec2(0.5)) * uAmplitude;
        float d = -uTime * 0.5 * uSpeed;
        float a = 0.0;
        for (float i = 0.0; i < 8.0; ++i) {
          a += cos(i - d - a * uv.x);
          d += sin(uv.y * i + a);
        }
        d += uTime * 0.5 * uSpeed;
        vec3 col = vec3(cos(uv * vec2(d, a)) * 0.6 + 0.4, cos(a + d) * 0.5 + 0.5);
        col = cos(col * cos(vec3(d, a, 2.5)) * 0.5 + 0.5) * uColor;
        gl_FragColor = vec4(col, 1.0);
      }
    `;

    const container = document.getElementById('iridescence-canvas');
    const renderer = new Renderer({ dpr: 2 });
    const gl = renderer.gl;
    container.appendChild(gl.canvas);

    gl.clearColor(1, 1, 1, 1);

    const geometry = new Triangle(gl);
    const program = new Program(gl, {
      vertex: vertexShader,
      fragment: fragmentShader,
      uniforms: {
        uTime: { value: 0 },
        uColor: { value: new Color(1, 1, 1) },
        uResolution: {
          value: new Color(gl.canvas.width, gl.canvas.height, gl.canvas.width / gl.canvas.height),
        },
        uMouse: { value: new Float32Array([0.5, 0.5]) },
        uAmplitude: { value: 0.1 },
        uSpeed: { value: 1.0 },
      },
    });

    const mesh = new Mesh(gl, { geometry, program });

    function resize() {
      renderer.setSize(container.offsetWidth, container.offsetHeight);
      program.uniforms.uResolution.value.set(gl.canvas.width, gl.canvas.height, gl.canvas.width / gl.canvas.height);
    }
    window.addEventListener('resize', resize, false);
    resize();

    // Cambios de color interpolados
    const colors = [
      [0.137, 0.215, 0.451], // Azul oscuro
      [1.0, 1.0, 1.0],       // Blanco
      [0.678, 0.847, 0.902]  // Celeste bebé
    ];
    let colorIndex = 0;
    let currentColor = colors[0];
    let nextColor = colors[1];
    let t = 0;
    const transitionSpeed = 0.005;

    function lerpColor(a, b, t) {
      return [
        a[0] + (b[0] - a[0]) * t,
        a[1] + (b[1] - a[1]) * t,
        a[2] + (b[2] - a[2]) * t,
      ];
    }

    function animate(time) {
      requestAnimationFrame(animate);
      program.uniforms.uTime.value = time * 0.001;

      // Color transition
      t += transitionSpeed;
      if (t >= 1) {
        t = 0;
        colorIndex = (colorIndex + 1) % colors.length;
        currentColor = nextColor;
        nextColor = colors[(colorIndex + 1) % colors.length];
      }
      const interpolated = lerpColor(currentColor, nextColor, t);
      program.uniforms.uColor.value.set(...interpolated);

      renderer.render({ scene: mesh });
    }
    animate(0);