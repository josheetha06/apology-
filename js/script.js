/**
 * A Heartfelt Apology - Translucent Editorial Pink Envelope Experience
 * Background Song Playback ('Aaruyire Mannippaya'), 'love love love' Calligraphy & Full Letter Reader
 */

(function () {
  'use strict';

  // --- Configuration ---
  const CONFIG = {
    theme: 'theme-blush-pink',
    salutation: 'Sanjay maa,',
    date: 'November 18, 2026',
    watermark: 'love love love',
    p1: `I am so sorry. Enna manichiru maa see I know how much you do for me enakkandi evlo pandra and evlo effort podra nu I know am sorry naan sonnadhu thappu I should have not said. The thing is sometimes I feel a lil extra and expect you to handle me at times like that I have told you too epdi easy ah you can do nu at that time I don't want lecture or logic ah explanation la I just want to be comforted Sanjay maa adhu dha nee purinjikkala nu soltu unta sanda podren. Andha ID naan sonna nee eduppa nu oru kutty aasai nee pannala nu kaduppu aagi dha moonja thookunen. And am sorry for not holding ur hand when you asked me I should have done that soothu koluppu eduthu I did not do sorry adhukku. Nee soldra neraya vishyam hurt aagum Sanju maa sanda apo so ennala adha easy ah let go panna mudila cause I don't expec those from you cause I am very vulnerable with you and enakulla edho ellaru maariyu ivanu nammala ipdi solla maatan seyya maatan nu so when you do that it hurts me and hard for me to let go enna manichiru.`,
    p2: `Enakku un kooda sanda poda theriyu unna katha theriyu konjo theriyu adikka theriyu aana unna vittu irukka therla Sanju maa. Yeah ego irukku neraya illa sollala but I don't hold onto things cause I have ego but because it hurt me cause my heart ku adhu unexpected. But it doesn't mean I've forgot what all you do for me Sanjay maa I love when you hold my hips while you talk to boys or when we walk, I love when you text me even when you are working or driving, I love when you text me you reached, I love when you send me cyut snaps of you and chunnu, I love when you smile when I make pee jokes, I love when you take bag from me no effort of urs go unnoticed by me Sanjay maa I always have eyes for you and you only na. I can't hate you Sanjay I can't unlove you I can't forget ur touch I can never na maa I just love you so much Sanjay.`,
    p3: `Un kooda pesama irukkanum avan vantu pesatum eppome naan dha pesuren nu thonum but adhunala enna koranjiduven nu irukkum so why I always come for you just sometimes kutty ah I have aasai avan vandhu pesanum enna miss pannanum thonanum nu irukkum am not able to help it na ponnu na maa. Enna manichiru maa I never meant to make ur life harder. Ishtam maa nee enakku eppome ishtam na kashtam irukkum na. Idk if you will read or reply to this but ellam sollanum thonichu solten maa. I still always think of us cuddling when I eep na it helps me eep in peace my heart and body always aches for you Sanju maa. I love you Sanjay. 💗`,
    signature: 'With Love & Regret'
  };

  // DOM Elements
  const progressBar = document.getElementById('progressBar');
  const envelopeBox = document.getElementById('envelopeBox');
  const envTopFlap = document.getElementById('envTopFlap');
  const waxSealWrapper = document.getElementById('waxSealWrapper');
  
  const itemLace = document.getElementById('itemLace');
  const itemVellum = document.getElementById('itemVellum');
  const itemPolaroid = document.getElementById('itemPolaroid');
  const itemLetter = document.getElementById('itemLetter');
  const envOrchid = document.getElementById('envOrchid');
  const interactionHint = document.getElementById('interactionHint');

  // Full Letter Modal Elements
  const fullLetterModal = document.getElementById('fullLetterModal');
  const closeLetterModalBtn = document.getElementById('closeLetterModalBtn');

  // Background Audio Elements
  const bgAudio = document.getElementById('bgAudio');
  const audioToggleBtn = document.getElementById('audioToggleBtn');
  const audioIcon = document.getElementById('audioIcon');
  const audioLabel = document.getElementById('audioLabel');

  let isMusicPlaying = true;
  let hasAttemptedAutoplay = false;

  // Animation Variables
  let currentScrollProgress = 0;
  let targetScrollProgress = 0;

  function clamp(val, min, max) {
    return Math.max(min, Math.min(max, val));
  }

  function lerp(start, end, factor) {
    return start + (end - start) * factor;
  }

  function mapRange(value, inMin, inMax, outMin, outMax) {
    const clamped = clamp(value, inMin, inMax);
    return outMin + ((clamped - inMin) / (inMax - inMin)) * (outMax - outMin);
  }

  function computeTargetScroll() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop || 0;
    const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    if (maxScroll <= 0) {
      targetScrollProgress = 0;
    } else {
      targetScrollProgress = clamp(scrollTop / maxScroll, 0, 1);
    }
  }

  function animate() {
    currentScrollProgress = lerp(currentScrollProgress, targetScrollProgress, 0.12);

    if (Math.abs(currentScrollProgress - targetScrollProgress) < 0.0005) {
      currentScrollProgress = targetScrollProgress;
    }

    renderEnvelopeState(currentScrollProgress);
    requestAnimationFrame(animate);
  }

  // --- Core 3D Rendering Function ---
  function renderEnvelopeState(p) {
    const isMobile = window.innerWidth <= 768;

    // 1. Progress Bar
    if (progressBar) {
      progressBar.style.width = (p * 100).toFixed(1) + '%';
    }

    // 2. Interaction Hint
    if (interactionHint) {
      if (p > 0.04) {
        interactionHint.classList.add('hidden');
      } else {
        interactionHint.classList.remove('hidden');
      }
    }

    // 3. Flap 3D Rotation & Wax Seal
    // - From p=0 to p=0.08: Flap is closed (0deg)
    // - From p=0.08 to p=0.38: Flap rotates 0deg -> 180deg
    // - When flapAngle > 90deg: Flap flips behind the envelope (zIndex = 1)
    let flapAngle = 0;
    let sealOpacity = 1;
    let sealScale = 1;

    if (p <= 0.08) {
      flapAngle = 0;
      sealOpacity = 1;
      sealScale = 1;
    } else if (p < 0.38) {
      flapAngle = mapRange(p, 0.08, 0.38, 0, 180);
      sealOpacity = mapRange(p, 0.08, 0.22, 1, 0);
      sealScale = mapRange(p, 0.08, 0.22, 1, 1.35);
    } else {
      flapAngle = 180;
      sealOpacity = 0;
      sealScale = 1.35;
    }

    if (envTopFlap) {
      envTopFlap.style.transform = `rotateX(${flapAngle.toFixed(2)}deg)`;
      
      // When flap passes 90 degrees, it flips behind the envelope
      if (flapAngle > 90) {
        envTopFlap.style.zIndex = '1';
      } else {
        envTopFlap.style.zIndex = '20';
      }
    }

    if (waxSealWrapper) {
      waxSealWrapper.style.opacity = sealOpacity.toFixed(2);
      waxSealWrapper.style.transform = `translate(-50%, 50%) scale(${sealScale.toFixed(2)})`;
      waxSealWrapper.style.pointerEvents = sealOpacity <= 0.1 ? 'none' : 'auto';
    }

    // 4. Inside Items Appearance
    const itemsOpacity = mapRange(p, 0.12, 0.36, 0, 1);
    
    // Item A: Lace Doily
    if (itemLace) {
      const laceY = mapRange(p, 0.12, 0.55, 30, isMobile ? -90 : -125);
      itemLace.style.transform = `translate3d(0, ${laceY.toFixed(1)}px, 0) scale(${isMobile ? 0.95 : 1.0})`;
      itemLace.style.opacity = itemsOpacity.toFixed(2);
    }

    // Item B: Green Vellum Note
    if (itemVellum) {
      const vellumY = mapRange(p, 0.14, 0.55, 30, isMobile ? -75 : -100);
      const vellumRot = mapRange(p, 0.14, 0.55, -8, -12);
      itemVellum.style.transform = `translate3d(0, ${vellumY.toFixed(1)}px, 0) rotate(${vellumRot.toFixed(1)}deg)`;
      itemVellum.style.opacity = itemsOpacity.toFixed(2);
    }

    // Item C: Polaroid
    if (itemPolaroid) {
      const polaroidY = mapRange(p, 0.14, 0.55, 30, isMobile ? -70 : -95);
      const polaroidRot = mapRange(p, 0.14, 0.55, 6, 9);
      itemPolaroid.style.transform = `translate3d(0, ${polaroidY.toFixed(1)}px, 0) rotate(${polaroidRot.toFixed(1)}deg)`;
      itemPolaroid.style.opacity = itemsOpacity.toFixed(2);
    }

    // Item D: The Peeking Letter Card
    if (itemLetter) {
      const letterPeekY = isMobile ? -90 : -130;
      const letterY = mapRange(p, 0.15, 0.65, 20, letterPeekY);
      const letterOpacity = mapRange(p, 0.10, 0.32, 0, 1);

      itemLetter.style.transform = `translate3d(0, ${letterY.toFixed(1)}px, 0)`;
      itemLetter.style.opacity = letterOpacity.toFixed(2);

      if (p > 0.38) {
        itemLetter.style.zIndex = '25';
      } else {
        itemLetter.style.zIndex = '5';
      }
    }

    // 5. Orchid Blossom subtle float
    if (envOrchid) {
      const orchidY = mapRange(p, 0.20, 0.80, 0, -6);
      const orchidRot = mapRange(p, 0.20, 0.80, -10, -7);
      envOrchid.style.transform = `translateY(${orchidY.toFixed(1)}px) rotate(${orchidRot.toFixed(1)}deg)`;
    }
  }

  // --- Full Letter Modal Functions ---
  function openFullLetter() {
    if (!fullLetterModal) return;
    fullLetterModal.classList.add('open');
    document.body.style.overflow = 'hidden';
    startMusicOnInteraction();
  }

  function closeFullLetter() {
    if (!fullLetterModal) return;
    fullLetterModal.classList.remove('open');
    document.body.style.overflow = '';
  }

  function openEnvelopeFully() {
    const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    window.scrollTo({
      top: maxScroll * 0.96,
      behavior: 'smooth'
    });
    startMusicOnInteraction();
  }

  // --- Background Song Playback Engine ---
  function playMusic() {
    if (!bgAudio) return;
    bgAudio.volume = 0.65;
    const playPromise = bgAudio.play();
    if (playPromise !== undefined) {
      playPromise.then(() => {
        isMusicPlaying = true;
        if (audioToggleBtn) audioToggleBtn.classList.add('playing');
        if (audioLabel) audioLabel.textContent = 'Music: Playing';
      }).catch(err => {
        console.log('Autoplay pending user gesture:', err);
      });
    }
  }

  function pauseMusic() {
    if (!bgAudio) return;
    bgAudio.pause();
    isMusicPlaying = false;
    if (audioToggleBtn) audioToggleBtn.classList.remove('playing');
    if (audioLabel) audioLabel.textContent = 'Music: Off';
  }

  function toggleMusic() {
    if (isMusicPlaying && !bgAudio.paused) {
      pauseMusic();
    } else {
      playMusic();
    }
  }

  function startMusicOnInteraction() {
    if (!isMusicPlaying || bgAudio.paused) {
      playMusic();
    }
  }

  // --- Ambient Canvas Falling Petals ---
  const canvas = document.getElementById('ambientCanvas');
  const ctx = canvas ? canvas.getContext('2d') : null;
  let particles = [];
  let canvasWidth = 0;
  let canvasHeight = 0;

  function resizeCanvas() {
    if (!canvas) return;
    canvasWidth = canvas.width = window.innerWidth;
    canvasHeight = canvas.height = window.innerHeight;
  }

  class Particle {
    constructor() {
      this.reset();
    }

    reset() {
      this.x = Math.random() * canvasWidth;
      this.y = -20 - Math.random() * 50;
      this.vx = (Math.random() - 0.5) * 0.8;
      this.vy = Math.random() * 0.8 + 0.4;
      this.alpha = Math.random() * 0.5 + 0.2;
      this.size = Math.random() * 8 + 6;
      this.rotation = Math.random() * Math.PI * 2;
      this.rotSpeed = (Math.random() - 0.5) * 0.03;
      const colors = ['#f7d6e0', '#f4acb7', '#f8edeb', '#ffcad4', '#eddcd2', '#ffd166'];
      this.color = colors[Math.floor(Math.random() * colors.length)];
    }

    update() {
      this.x += this.vx;
      this.y += this.vy;
      this.rotation += this.rotSpeed;
      this.vx += Math.sin(this.y * 0.01) * 0.02;
      if (this.y > canvasHeight + 20) {
        this.reset();
      }
    }

    draw(ctx) {
      if (this.alpha <= 0) return;
      ctx.save();
      ctx.translate(this.x, this.y);
      ctx.rotate(this.rotation);
      ctx.globalAlpha = Math.max(0, this.alpha);
      ctx.fillStyle = this.color;

      ctx.beginPath();
      ctx.moveTo(0, -this.size / 2);
      ctx.bezierCurveTo(this.size / 2, -this.size / 2, this.size / 2, this.size / 2, 0, this.size);
      ctx.bezierCurveTo(-this.size / 2, this.size / 2, -this.size / 2, -this.size / 2, 0, -this.size / 2);
      ctx.fill();

      ctx.restore();
    }
  }

  function initParticles() {
    if (!ctx) return;
    particles = [];
    const count = window.innerWidth <= 768 ? 16 : 28;
    for (let i = 0; i < count; i++) {
      const p = new Particle();
      p.y = Math.random() * canvasHeight;
      particles.push(p);
    }
  }

  function renderParticles() {
    if (!ctx) return;
    ctx.clearRect(0, 0, canvasWidth, canvasHeight);

    for (let i = particles.length - 1; i >= 0; i--) {
      const p = particles[i];
      p.update();
      p.draw(ctx);
    }

    requestAnimationFrame(renderParticles);
  }

  // --- Event Listeners ---
  function setupEvents() {
    window.addEventListener('scroll', computeTargetScroll, { passive: true });
    window.addEventListener('resize', () => {
      resizeCanvas();
      computeTargetScroll();
    });

    // Peeking letter card click -> Open full letter reader!
    if (itemLetter) {
      itemLetter.addEventListener('click', (e) => {
        e.stopPropagation();
        openFullLetter();
      });
    }

    if (closeLetterModalBtn) {
      closeLetterModalBtn.addEventListener('click', closeFullLetter);
    }

    if (fullLetterModal) {
      fullLetterModal.addEventListener('click', (e) => {
        if (e.target === fullLetterModal) {
          closeFullLetter();
        }
      });
    }

    // Envelope click action (when closed)
    if (envelopeBox) {
      envelopeBox.addEventListener('click', (e) => {
        if (e.target.closest('#itemLetter')) return;
        
        if (currentScrollProgress < 0.2) {
          openEnvelopeFully();
        }
      });
    }

    // Audio button click
    if (audioToggleBtn) {
      audioToggleBtn.addEventListener('click', toggleMusic);
    }

    if (interactionHint) {
      interactionHint.addEventListener('click', openEnvelopeFully);
    }

    // Start music immediately and unlock on any first interaction
    const interactionEvents = ['pointerdown', 'mousedown', 'touchstart', 'scroll', 'wheel', 'keydown', 'mousemove'];
    function unlockAudio() {
      playMusic();
      interactionEvents.forEach(evt => window.removeEventListener(evt, unlockAudio));
    }
    interactionEvents.forEach(evt => window.addEventListener(evt, unlockAudio, { passive: true }));

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeFullLetter();
      }
    });
  }

  // --- Initialize ---
  function init() {
    document.body.className = CONFIG.theme;
    resizeCanvas();
    initParticles();
    renderParticles();
    setupEvents();
    computeTargetScroll();
    animate();
    playMusic();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
