
<template>
  <div>
    <div
      class="layout"
      id="upload-loading"
    >
      <div class="container-loading1">
        <div></div>
      </div>
    </div>
  </div>

</template>

 <script>
export default {
  name: "upload-loading2",
  data () {
    load = {};
  },
  methods: {
    init () {
      window.$load = {};

      window.$load.Particle = function (opt) {
        this.radius = 7;
        this.x = opt.x;
        this.y = opt.y;
        this.angle = opt.angle;
        this.speed = opt.speed;
        this.accel = opt.accel;
        this.decay = 0.01;
        this.life = 1;
      };

      window.$load.Particle.prototype.step = function (i) {
        this.speed += this.accel;
        this.x += Math.cos(this.angle) * this.speed;
        this.y += Math.sin(this.angle) * this.speed;
        this.angle += window.$load.PI / 64;
        this.accel *= 1.01;
        this.life -= this.decay;

        if (this.life <= 0) {
          window.$load.particles.splice(i, 1);
        }
      };

      window.$load.Particle.prototype.draw = function (i) {
        window.$load.ctx.fillStyle = window.$load.ctx.strokeStyle = 'hsla(' + (window.$load.tick + (this.life * 120)) +
          ', 100%, 60%, ' + this.life + ')';
        window.$load.ctx.beginPath();
        if (window.$load.particles[i - 1]) {
          window.$load.ctx.moveTo(this.x, this.y);
          window.$load.ctx.lineTo(window.$load.particles[i - 1].x, window.$load.particles[i - 1].y);
        }
        window.$load.ctx.stroke();

        window.$load.ctx.beginPath();
        window.$load.ctx.arc(this.x, this.y, Math.max(0.001, this.life * this.radius), 0, window.$load.TWO_PI);
        window.$load.ctx.fill();

        var size = Math.random() * 1.25;
        window.$load.ctx.fillRect(~~(this.x + ((Math.random() - 0.5) * 35) * this.life), ~~(this.y + ((Math.random() -
          0.5) * 35) * this.life), size, size);
      }

      window.$load.step = function () {
        window.$load.particles.push(new window.$load.Particle({
          x: window.$load.width / 2 + Math.cos(window.$load.tick / 20) * window.$load.min / 2,
          y: window.$load.height / 2 + Math.sin(window.$load.tick / 20) * window.$load.min / 2,
          angle: window.$load.globalRotation + window.$load.globalAngle,
          speed: 0,
          accel: 0.01
        }));

        window.$load.particles.forEach(function (elem, index) {
          elem.step(index);
        });

        window.$load.globalRotation += window.$load.PI / 6;
        window.$load.globalAngle += window.$load.PI / 6;
      };

      window.$load.draw = function () {
        window.$load.ctx.clearRect(0, 0, window.$load.width, window.$load.height);

        window.$load.particles.forEach(function (elem, index) {
          elem.draw(index);
        });
      };

      window.$load.init = function () {
        window.$load.canvas = document.createElement('canvas');
        window.$load.ctx = window.$load.canvas.getContext('2d');
        window.$load.width = 300;
        window.$load.height = 300;
        window.$load.canvas.width = window.$load.width * window.devicePixelRatio;
        window.$load.canvas.height = window.$load.height * window.devicePixelRatio;
        window.$load.canvas.style.width = window.$load.width + 'px';
        window.$load.canvas.style.height = window.$load.height + 'px';
        window.$load.ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
        window.$load.min = window.$load.width * 0.5;
        window.$load.particles = [];
        window.$load.globalAngle = 0;
        window.$load.globalRotation = 0;
        window.$load.tick = 0;
        window.$load.PI = Math.PI;
        window.$load.TWO_PI = window.$load.PI * 2;
        window.$load.ctx.globalCompositeOperation = 'lighter';
        document.getElementsByClassName("container-loading1")[0].appendChild(window.$load.canvas);
        window.$load.loop();
      };

      window.$load.loop = function () {
        requestAnimationFrame(window.$load.loop);
        window.$load.step();
        window.$load.draw();
        window.$load.tick++;
      };

    },
    loop () {

      window.$load.init();
    }


  },
  mounted () {
    this.init();
    window.$load.init();
  }
}

</script>

<style scoped>
#upload-loading {
  display: none;
}

.container-loading1 {
  -moz-opacity: 0.5;
  filter: alpha(opacity=50);
  position: fixed;
  left: 0;
  top: 0;
  width: calc(100vw);
  height: 100%;
  background-color: rgba(255, 255, 255, 0.5);
  z-index: 10000;
  display: flex;
  align-items: center;
  justify-content: center;
}
canvas {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
}
</style>