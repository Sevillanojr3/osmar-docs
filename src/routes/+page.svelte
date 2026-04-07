<script lang="ts">
	import { onMount } from 'svelte';
	import content from '$lib/content.json';

	const d = content.sections;

	if (typeof window !== 'undefined') {
		window.history.scrollRestoration = 'manual';
		window.scrollTo(0, 0);
	}

	onMount(async () => {
		const { gsap } = await import('gsap');
		const { ScrollTrigger } = await import('gsap/ScrollTrigger');
		gsap.registerPlugin(ScrollTrigger);

		window.scrollTo(0, 0);
		window.addEventListener('beforeunload', () => window.scrollTo(0, 0));

		gsap.defaults({ ease: 'power3.out' });

		// === HERO ===
		const h = gsap.timeline({ delay: 0.2 });
		h.from('.hero-logo', { autoAlpha: 0, scale: 0.5, duration: 1, ease: 'back.out(1.7)' })
		 .from('.hero-badge', { autoAlpha: 0, y: 30, duration: 0.6 }, '-=0.5')
		 .from('.hero-title .word', { autoAlpha: 0, y: 100, stagger: 0.1, duration: 1 }, '-=0.4')
		 .from('.hero-sub', { autoAlpha: 0, y: 40, duration: 0.8 }, '-=0.5')
		 .from('.hero-scroll', { autoAlpha: 0, duration: 0.6 }, '-=0.3');
		gsap.to('.hero-logo', { y: -15, duration: 3, repeat: -1, yoyo: true, ease: 'sine.inOut' });

		// === PINNED SECTION HELPER ===
		function pin(id: string, end: string, fn: (t: gsap.core.Timeline) => void) {
			const t = gsap.timeline({
				scrollTrigger: { trigger: `#${id}`, start: 'top top', end: `+=${end}`, pin: true, scrub: 1, anticipatePin: 1 }
			});
			fn(t);
			t.to({}, { duration: 0.5 });
		}

		// === PROBLEM ===
		pin('problem', '200%', t => {
			t.from('.p-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.p-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.p-dsc', { autoAlpha: 0, y: 40 }, 0.3)
			 .from('.p-img', { autoAlpha: 0, scale: 0.6, rotation: -3, duration: 0.8, ease: 'power2.out' }, 0.2)
			 .from('.p-bdg', { autoAlpha: 0, scale: 0, stagger: 0.04, duration: 0.25, ease: 'back.out(1.7)' }, 0.6);
		});

		// === PHILOSOPHY ===
		pin('philosophy', '220%', t => {
			t.from('.ph-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.ph-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.ph-dsc', { autoAlpha: 0, y: 40 }, 0.3)
			 .from('.ph-img', { autoAlpha: 0, scale: 0.7, duration: 0.8 }, 0.2)
			 .from('.ph-hi', { autoAlpha: 0, y: 30 }, 0.5)
			 .from('.ph-l', { autoAlpha: 0, x: -80, duration: 0.6 }, 0.65)
			 .from('.ph-r', { autoAlpha: 0, x: 80, duration: 0.6 }, 0.65);
		});

		// === TWO KEYS ===
		pin('twokeys', '180%', t => {
			t.from('.tk-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.tk-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.tk-card', { autoAlpha: 0, y: 50, stagger: 0.15, duration: 0.5 }, 0.3);
		});

		// === INGREDIENTS ===
		pin('ingredients', '300%', t => {
			t.from('.in-step', { autoAlpha: 0, scale: 0.3, duration: 0.5, ease: 'back.out(2)' }, 0)
			 .from('.in-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.2)
			 .from('.in-dsc', { autoAlpha: 0, y: 40 }, 0.4)
			 .from('.in-img', { autoAlpha: 0, x: -60, duration: 0.7 }, 0.3)
			 .from('.in-r0', { autoAlpha: 0, x: 60, duration: 0.5 }, 0.6)
			 .from('.in-r1', { autoAlpha: 0, x: -60, duration: 0.5 }, 0.85)
			 .from('.in-r2', { autoAlpha: 0, x: 60, duration: 0.5 }, 1.1);
		});

		// === SUGAR ===
		pin('sugar', '300%', t => {
			t.from('.su-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.su-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.su-dsc', { autoAlpha: 0, y: 30 }, 0.3)
			 .from('.su-img', { autoAlpha: 0, scale: 0.5, duration: 0.8 }, 0.2)
			 .from('.su-cnt', { autoAlpha: 0, scale: 0, duration: 0.6, ease: 'back.out(2)' }, 0.5)
			 .from('.su-pill', { autoAlpha: 0, scale: 0.3, stagger: { each: 0.012, from: 'random' }, duration: 0.2, ease: 'back.out(1.5)' }, 0.7)
			 .from('.su-fn', { autoAlpha: 0 }, 1.1);
		});
		ScrollTrigger.create({
			trigger: '#sugar', start: 'top top', end: '+=300%', scrub: true,
			onUpdate: s => { const e = document.querySelector('.su-cnt') as HTMLElement; if(e) { const v=Math.floor(gsap.utils.clamp(0,17,gsap.utils.mapRange(0.2,0.5,0,17,s.progress))); e.textContent=v+''; } }
		});

		// === MARKETING ===
		pin('marketing', '250%', t => {
			t.from('.mk-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.mk-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.mk-img', { autoAlpha: 0, scale: 0.7, duration: 0.7 }, 0.15)
			 .from('.mk-cd', { autoAlpha: 0, y: 60, stagger: 0.1, duration: 0.5 }, 0.4);
		});

		// === SODIUM ===
		pin('sodium', '200%', t => {
			t.from('.so-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.so-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.so-dsc', { autoAlpha: 0, y: 30 }, 0.3)
			 .from('.so-bar', { autoAlpha: 0, x: -40, stagger: 0.1, duration: 0.4 }, 0.4)
			 .from('.so-fill', { scaleX: 0, transformOrigin: 'left center', stagger: 0.1, duration: 0.5 }, 0.5)
			 .from('.so-fn', { autoAlpha: 0 }, 0.9);
		});

		// === CARBS ===
		pin('carbs', '350%', t => {
			t.from('.cb-tag', { autoAlpha: 0, y: 20 }, 0)
			 .from('.cb-ttl', { autoAlpha: 0, y: 40, duration: 0.6 }, 0.1)
			 .from('.cb-dsc', { autoAlpha: 0, y: 30 }, 0.3)
			 .from('.cb-b0', { autoAlpha: 0, y: 60, duration: 0.5 }, 0.5)
			 .from('.cb-b1', { autoAlpha: 0, y: 60, duration: 0.5 }, 0.8)
			 .from('.cb-b2', { autoAlpha: 0, y: 60, duration: 0.5 }, 1.1);
		});

		// === FATS ===
		pin('fats', '250%', t => {
			t.from('.ft-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.ft-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.ft-dsc', { autoAlpha: 0, y: 30 }, 0.3)
			 .from('.ft-gd', { autoAlpha: 0, x: -60, duration: 0.6 }, 0.5)
			 .from('.ft-bd', { autoAlpha: 0, x: 60, duration: 0.6 }, 0.5)
			 .from('.ft-lm', { autoAlpha: 0, y: 30, stagger: 0.1, duration: 0.4 }, 0.8)
			 .from('.ft-fn', { autoAlpha: 0 }, 1.0);
		});

		// === CALORIES ===
		pin('calories', '150%', t => {
			t.from('.cal-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.cal-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.cal-dsc', { autoAlpha: 0, y: 30 }, 0.3);
		});

		// === MACROS ===
		pin('macros', '220%', t => {
			t.from('.ma-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.ma-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.ma-dsc', { autoAlpha: 0, y: 30 }, 0.3)
			 .from('.ma-img', { autoAlpha: 0, scale: 0.7, duration: 0.7 }, 0.2)
			 .from('.ma-dt', { autoAlpha: 0, y: 30, duration: 0.5 }, 0.5)
			 .from('.ma-ex', { autoAlpha: 0, y: 30, duration: 0.5 }, 0.7);
		});

		// === PORTIONS ===
		pin('portions', '250%', t => {
			t.from('.po-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.po-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.po-img', { autoAlpha: 0, scale: 0.7, duration: 0.7 }, 0.15)
			 .from('.po-row', { autoAlpha: 0, x: 50, stagger: 0.08, duration: 0.4 }, 0.4);
		});

		// === PRACTICE ===
		pin('practice', '300%', t => {
			t.from('.pr-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.pr-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
			 .from('.pr-dsc', { autoAlpha: 0, y: 30 }, 0.3)
			 .from('.pr-lb', { autoAlpha: 0, y: 80, scale: 0.9, duration: 0.8, ease: 'power2.out' }, 0.4)
			 .from('.pr-cl', { autoAlpha: 0, y: 50, duration: 0.6 }, 0.8);
		});

		// === CLOSING ===
		pin('closing', '250%', t => {
			t.from('.cl-logo', { autoAlpha: 0, scale: 0.5, duration: 0.7, ease: 'back.out(1.7)' }, 0)
			 .from('.cl-ttl', { autoAlpha: 0, y: 100, duration: 0.7 }, 0.2)
			 .from('.cl-dsc', { autoAlpha: 0, y: 40, duration: 0.5 }, 0.5)
			 .from('.cl-hi', { autoAlpha: 0, y: 30, duration: 0.5 }, 0.7)
			 .from('.cl-cta', { autoAlpha: 0, y: 40, scale: 0.9, duration: 0.5, ease: 'back.out(1.7)' }, 0.9)
			 .from('.cl-auth', { autoAlpha: 0, duration: 0.5 }, 1.1);
		});

		return () => { ScrollTrigger.getAll().forEach(t => t.kill()); };
	});
</script>

<svelte:head><title>{content.meta.title}</title></svelte:head>

<!-- HERO -->
<section id="hero" class="relative flex h-screen flex-col items-center justify-center overflow-hidden px-4 sm:px-6">
	<!-- global bg from css -->
	<div class="pointer-events-none absolute inset-0"><div class="absolute top-1/4 left-1/2 h-[800px] w-[800px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-[#4CAF50]/10 blur-[160px]"></div></div>
	<img src="/images/logo-sm.webp" alt="Coach BattleBeast" class="hero-logo mb-4 h-28 w-auto rounded-2xl object-contain sm:mb-6 sm:h-40 md:h-52" />
	<span class="hero-badge mb-4 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-xs font-medium tracking-[0.2em] text-[#81C784] uppercase sm:mb-6 sm:px-6 sm:py-2.5 sm:text-sm">{d[0].badge}</span>
	<h1 class="hero-title max-w-5xl text-center text-4xl leading-[1.05] font-extrabold tracking-tight text-white sm:text-5xl md:text-7xl lg:text-8xl xl:text-9xl">
		{#each d[0].title.split(' ') as w}<span class="word inline-block">{w}&nbsp;</span>{/each}
	</h1>
	<p class="hero-sub mt-4 max-w-xl text-center text-base leading-relaxed text-white/40 sm:mt-8 sm:text-xl">{d[0].subtitle}</p>
	<div class="hero-scroll mt-8 flex flex-col items-center gap-2 text-white/20 sm:mt-16"><span class="text-[10px] tracking-[0.3em] uppercase">Scroll</span><svg class="h-5 w-5 animate-bounce" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19 14l-7 7m0 0l-7-7m7 7V3"/></svg></div>
</section>

<!-- PROBLEM -->
<section id="problem" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="flex max-w-6xl flex-col items-center gap-6 sm:gap-10 md:flex-row">
		<img src="/images/problem.webp" loading="lazy" decoding="async" alt="" class="p-img h-40 w-40 flex-shrink-0 rounded-3xl object-cover shadow-2xl shadow-black/50 sm:h-64 sm:w-64 md:h-80 md:w-80" />
		<div class="text-center md:text-left">
			<span class="p-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase sm:mb-3">{d[1].tagline}</span>
			<h2 class="p-ttl text-3xl font-bold text-white sm:text-4xl md:text-5xl lg:text-6xl">{d[1].title}</h2>
			<p class="p-dsc mt-3 max-w-lg text-base leading-relaxed text-white/40 sm:mt-5 sm:text-lg">{d[1].description}</p>
			<div class="mt-4 flex flex-wrap justify-center gap-2 sm:mt-6 sm:gap-2.5 md:justify-start">
				{#each d[1].badges as b}<span class="p-bdg rounded-full border border-red-500/20 bg-red-500/8 px-3 py-1.5 text-xs text-red-400/80 sm:px-4 sm:py-2 sm:text-sm">{b}</span>{/each}
			</div>
		</div>
	</div>
</section>

<!-- PHILOSOPHY -->
<section id="philosophy" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="flex max-w-6xl flex-col items-center gap-6 sm:gap-10 md:flex-row-reverse">
		<img src="/images/philosophy.webp" loading="lazy" decoding="async" alt="" class="ph-img h-40 w-40 flex-shrink-0 rounded-3xl object-cover shadow-2xl shadow-black/50 sm:h-64 sm:w-64 md:h-80 md:w-80" />
		<div class="text-center md:text-left">
			<span class="ph-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase sm:mb-3">{d[2].tagline}</span>
			<h2 class="ph-ttl text-3xl font-bold text-white sm:text-4xl md:text-5xl lg:text-6xl">{d[2].title}</h2>
			<p class="ph-dsc mt-3 max-w-lg text-base leading-relaxed text-white/40 sm:mt-4 sm:text-lg">{d[2].description}</p>
			<p class="ph-hi mt-3 rounded-xl border border-[#4CAF50]/10 bg-[#4CAF50]/5 px-4 py-3 text-xs leading-relaxed text-[#81C784] sm:mt-4 sm:px-5 sm:py-4 sm:text-sm">{d[2].highlight}</p>
			<div class="mt-5 flex items-center justify-center gap-6 sm:mt-8 sm:gap-8 md:justify-start">
				<div class="ph-l flex flex-col items-center"><span class="text-4xl font-black text-[#4CAF50] sm:text-5xl md:text-6xl">80%</span><span class="text-[10px] text-white/30 uppercase sm:text-xs">Nutritivo</span></div>
				<div class="h-10 w-px bg-white/10 sm:h-14"></div>
				<div class="ph-r flex flex-col items-center"><span class="text-4xl font-black text-[#FF9800] sm:text-5xl md:text-6xl">20%</span><span class="text-[10px] text-white/30 uppercase sm:text-xs">Flexible</span></div>
			</div>
		</div>
	</div>
</section>

<!-- TWO KEYS -->
<section id="twokeys" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="max-w-4xl text-center">
		<span class="tk-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase sm:mb-3">{d[3].tagline}</span>
		<h2 class="tk-ttl mb-6 text-3xl font-bold text-white sm:mb-12 sm:text-4xl md:text-5xl lg:text-6xl">{d[3].title}</h2>
		<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 sm:gap-6">
			{#each d[3].items as item}
				<div class="tk-card rounded-2xl border border-white/5 bg-white/[0.03] p-5 text-left sm:p-8">
					<span class="mb-2 block text-4xl font-black text-[#4CAF50]/25 sm:mb-3 sm:text-5xl">{item.number}</span>
					<h3 class="text-lg font-semibold text-white sm:text-xl">{item.name}</h3>
					<p class="mt-1.5 text-sm leading-relaxed text-white/40 sm:mt-2 sm:text-base">{item.detail}</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- INGREDIENTS -->
<section id="ingredients" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="flex max-w-6xl flex-col items-center gap-5 sm:gap-8 md:flex-row">
		<div class="flex flex-shrink-0 flex-col items-center">
			<div class="in-step mb-3 flex h-14 w-14 items-center justify-center rounded-xl border border-[#4CAF50]/20 bg-[#4CAF50]/8 text-2xl font-black text-[#4CAF50] sm:mb-4 sm:h-20 sm:w-20 sm:rounded-2xl sm:text-3xl">01</div>
			<img src="/images/ingredients.webp" loading="lazy" decoding="async" alt="" class="in-img h-36 w-36 rounded-3xl object-cover shadow-2xl shadow-black/50 sm:h-52 sm:w-52 md:h-72 md:w-72" />
		</div>
		<div class="text-center md:text-left">
			<h2 class="in-ttl text-3xl font-bold text-white sm:text-4xl md:text-5xl">{d[4].title}</h2>
			<p class="in-dsc mt-2 max-w-lg text-sm leading-relaxed text-white/40 sm:mt-4 sm:text-base">{d[4].description}</p>
			<div class="mt-4 flex flex-col gap-2 sm:mt-6 sm:gap-3">
				{#each d[4].rules as rule, i}
					<div class="in-r{i} flex items-start gap-3 rounded-xl border border-white/5 bg-white/[0.03] p-3 text-left sm:gap-4 sm:p-5">
						<div class="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-lg bg-[#4CAF50]/10 sm:h-9 sm:w-9">
							<svg class="h-3.5 w-3.5 text-[#4CAF50] sm:h-4 sm:w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
								{#if rule.icon==='arrow-down'}<path stroke-linecap="round" stroke-linejoin="round" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>{:else if rule.icon==='list'}<path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h8m-8 6h16"/>{:else}<path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/>{/if}
							</svg>
						</div>
						<div><h3 class="text-sm font-semibold text-white sm:text-base">{rule.name}</h3><p class="mt-0.5 text-xs leading-relaxed text-white/40 sm:mt-1 sm:text-sm">{rule.detail}</p></div>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>

<!-- SUGAR -->
<section id="sugar" class="relative flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="pointer-events-none absolute inset-0"><div class="absolute top-1/2 left-1/2 h-[700px] w-[700px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-red-500/6 blur-[150px]"></div></div>
	<div class="max-w-5xl text-center">
		<span class="su-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-red-400 uppercase sm:mb-3">{d[5].tagline}</span>
		<h2 class="su-ttl text-3xl font-bold text-white sm:text-4xl md:text-5xl lg:text-6xl">{d[5].title}</h2>
		<p class="su-dsc mx-auto mt-2 max-w-2xl text-sm text-white/40 sm:mt-4 sm:text-base">{d[5].description}</p>
		<img src="/images/sugar.webp" loading="lazy" decoding="async" alt="" class="su-img mx-auto mt-4 h-28 w-28 rounded-2xl object-cover shadow-2xl shadow-red-900/30 sm:mt-6 sm:h-40 sm:w-40 md:h-48 md:w-48" />
		<span class="su-cnt mt-2 block text-6xl font-black text-red-400 tabular-nums sm:mt-4 sm:text-8xl md:text-9xl">0</span>
		<span class="text-xs tracking-wider text-white/30 uppercase sm:text-sm">{d[5].countLabel}</span>
		<div class="mx-auto mt-4 flex max-w-2xl flex-wrap justify-center gap-1.5 sm:mt-6 sm:gap-2">
			{#each d[5].hiddenNames as n}<span class="su-pill rounded-full border border-red-500/15 bg-red-500/8 px-2.5 py-1 text-[10px] text-red-400/70 sm:px-3 sm:py-1.5 sm:text-xs">{n}</span>{/each}
		</div>
		<p class="su-fn mx-auto mt-4 max-w-lg text-[10px] text-white/20 italic leading-relaxed sm:mt-6 sm:text-xs">{d[5].footnote}</p>
	</div>
</section>

<!-- MARKETING -->
<section id="marketing" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="max-h-[90vh] max-w-5xl overflow-y-auto text-center scrollbar-hide md:max-h-none md:overflow-visible">
		<span class="mk-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase sm:mb-3">{d[6].tagline}</span>
		<h2 class="mk-ttl text-2xl font-bold text-white sm:text-3xl md:text-5xl">{d[6].title}</h2>
		<p class="mt-1.5 text-[11px] text-white/40 sm:mt-3 sm:text-sm md:text-base">{d[6].description}</p>
		<img src="/images/marketing.webp" loading="lazy" decoding="async" alt="" class="mk-img mx-auto mt-3 hidden w-full max-w-xl rounded-2xl object-cover shadow-2xl shadow-black/50 sm:mt-6 sm:block sm:h-40" />
		<div class="mt-3 grid w-full grid-cols-2 gap-2 sm:mt-8 sm:gap-4">
			{#each d[6].items as item}
				<div class="mk-cd rounded-xl border border-white/5 bg-white/[0.03] p-2.5 text-left transition-colors hover:border-[#4CAF50]/20 hover:bg-white/[0.05] sm:p-4 md:p-6">
					<span class="mb-1 inline-block rounded-md bg-[#4CAF50]/10 px-2 py-0.5 text-[9px] font-bold tracking-wider text-[#4CAF50] uppercase sm:mb-2 sm:px-3 sm:py-1 sm:text-xs">{item.label}</span>
					<p class="text-[10px] leading-snug text-white/50 sm:text-xs md:text-sm">{item.truth}</p>
					<p class="mt-1 border-t border-white/5 pt-1 text-[9px] text-[#FF9800]/50 sm:mt-2 sm:pt-2 sm:text-xs">{item.warning}</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- SODIUM -->
<section id="sodium" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="max-w-3xl text-center">
		<span class="so-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#FF9800] uppercase sm:mb-3">{d[7].tagline}</span>
		<h2 class="so-ttl text-3xl font-bold text-white sm:text-4xl md:text-5xl lg:text-6xl">{d[7].title}</h2>
		<p class="so-dsc mt-2 text-sm text-white/40 sm:mt-4 sm:text-base">{d[7].description}</p>
		<div class="mx-auto mt-6 flex w-full max-w-lg flex-col gap-4 sm:mt-10 sm:gap-5">
			{#each d[7].levels as lv}
				<div class="so-bar text-left"><div class="mb-1 flex justify-between"><span class="text-xs font-medium text-white/70 sm:text-sm">{lv.label}</span><span class="text-[10px] text-white/40 sm:text-xs">{lv.value}</span></div>
				<div class="h-2.5 w-full overflow-hidden rounded-full bg-white/5 sm:h-3"><div class="so-fill h-full rounded-full" style="background:{lv.color};width:{lv.color==='#4CAF50'?'15%':lv.color==='#81C784'?'30%':lv.color==='#FF9800'?'55%':'80%'}"></div></div></div>
			{/each}
		</div>
		<p class="so-fn mt-4 text-[10px] text-white/20 italic leading-relaxed sm:mt-6 sm:text-xs">{d[7].footnote}</p>
	</div>
</section>

<!-- CARBS -->
<section id="carbs" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="max-h-[90vh] max-w-3xl overflow-y-auto text-center scrollbar-hide md:max-h-none md:overflow-visible">
		<span class="cb-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase sm:mb-3">{d[8].tagline}</span>
		<h2 class="cb-ttl text-2xl font-bold text-white sm:text-3xl md:text-5xl">{d[8].title}</h2>
		<p class="cb-dsc mt-1.5 text-[11px] text-white/40 sm:mt-4 sm:text-sm md:text-base">{d[8].description}</p>
		<div class="mt-2.5 flex w-full flex-col gap-2 sm:mt-8 sm:gap-4">
			{#each d[8].subsections as sub, i}
				<div class="cb-b{i} rounded-xl border border-white/5 bg-white/[0.03] p-2.5 text-left sm:p-5">
					<h3 class="text-xs font-semibold text-white sm:text-sm md:text-base">{sub.name}</h3>
					<p class="mt-0.5 text-[10px] leading-snug text-white/40 sm:mt-1.5 sm:text-xs md:text-sm">{sub.detail}</p>
					<div class="mt-1 rounded-lg bg-[#4CAF50]/5 px-2 py-1 sm:mt-3 sm:px-4 sm:py-2"><p class="text-[10px] font-medium text-[#4CAF50] sm:text-xs md:text-sm">{sub.rule}</p></div>
					{#if sub.limit}<p class="mt-0.5 text-[9px] leading-snug text-[#FF9800]/50 sm:mt-2 sm:text-xs">{sub.limit}</p>{/if}
					{#if sub.tip}<p class="mt-0.5 text-[9px] leading-snug text-[#2196F3]/50 sm:mt-1.5 sm:text-xs">Tip: {sub.tip}</p>{/if}
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- FATS -->
<section id="fats" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="max-w-3xl text-center">
		<span class="ft-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#FF9800] uppercase sm:mb-3">{d[9].tagline}</span>
		<h2 class="ft-ttl text-3xl font-bold text-white sm:text-4xl md:text-5xl">{d[9].title}</h2>
		<p class="ft-dsc mt-2 text-sm text-white/40 sm:mt-4 sm:text-base">{d[9].description}</p>
		<div class="mt-4 grid w-full grid-cols-1 gap-3 sm:mt-8 sm:grid-cols-2 sm:gap-4">
			<div class="ft-gd rounded-xl border border-[#4CAF50]/10 bg-[#4CAF50]/5 p-4 text-left sm:p-5">
				<h3 class="mb-2 text-[10px] font-bold tracking-wider text-[#4CAF50] uppercase sm:mb-3 sm:text-xs">Priorizar</h3>
				{#each d[9].good as g}<div class="mb-1.5 flex items-center gap-2 sm:mb-2"><div class="h-1.5 w-1.5 rounded-full bg-[#4CAF50] sm:h-2 sm:w-2"></div><span class="text-xs text-white/60 sm:text-sm">{g}</span></div>{/each}
			</div>
			<div class="ft-bd rounded-xl border border-red-500/10 bg-red-500/5 p-4 text-left sm:p-5">
				<h3 class="mb-2 text-[10px] font-bold tracking-wider text-red-400 uppercase sm:mb-3 sm:text-xs">Evitar frecuente</h3>
				{#each d[9].bad as b}<div class="mb-1.5 flex items-center gap-2 sm:mb-2"><div class="h-1.5 w-1.5 rounded-full bg-red-400 sm:h-2 sm:w-2"></div><span class="text-xs text-white/60 sm:text-sm">{b}</span></div>{/each}
			</div>
		</div>
		<div class="mt-3 flex flex-wrap justify-center gap-2 sm:mt-5 sm:gap-3">
			{#each d[9].limits as l}<div class="ft-lm rounded-lg border border-white/5 bg-white/[0.03] px-3 py-2 text-center sm:px-4 sm:py-2.5"><span class="text-[10px] font-bold uppercase sm:text-xs" style="color:{l.color}">{l.type}</span><p class="mt-0.5 text-[10px] text-white/40 sm:text-xs">{l.limit}</p></div>{/each}
		</div>
		<p class="ft-fn mt-3 text-[10px] text-white/20 italic leading-relaxed sm:mt-5 sm:text-xs">{d[9].footnote}</p>
	</div>
</section>

<!-- CALORIES -->
<section id="calories" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="max-w-3xl text-center">
		<span class="cal-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase sm:mb-3">{d[10].tagline}</span>
		<h2 class="cal-ttl text-3xl font-bold text-white sm:text-4xl md:text-5xl lg:text-7xl">{d[10].title}</h2>
		<p class="cal-dsc mx-auto mt-4 max-w-xl text-base leading-relaxed text-white/40 sm:mt-6 sm:text-xl">{d[10].description}</p>
	</div>
</section>

<!-- MACROS -->
<section id="macros" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="flex max-w-6xl flex-col items-center gap-5 sm:gap-8 md:flex-row">
		<img src="/images/macros.webp" loading="lazy" decoding="async" alt="" class="ma-img h-40 w-40 flex-shrink-0 rounded-3xl object-cover shadow-2xl shadow-black/50 sm:h-60 sm:w-60 md:h-80 md:w-80" />
		<div class="text-center md:text-left">
			<span class="ma-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase sm:mb-3">{d[11].tagline}</span>
			<h2 class="ma-ttl text-3xl font-bold text-white sm:text-4xl md:text-5xl">{d[11].title}</h2>
			<p class="ma-dsc mt-2 max-w-lg text-sm leading-relaxed text-white/40 sm:mt-4 sm:text-base">{d[11].description}</p>
			<p class="ma-dt mt-2 max-w-lg text-xs leading-relaxed text-white/30 sm:mt-4 sm:text-sm">{d[11].detail}</p>
			<div class="ma-ex mt-3 rounded-xl border border-white/5 bg-white/[0.03] px-4 py-3 sm:mt-4 sm:px-5 sm:py-4"><p class="text-xs leading-relaxed text-white/50 sm:text-sm">{d[11].example}</p></div>
		</div>
	</div>
</section>

<!-- PORTIONS -->
<section id="portions" class="flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="flex max-w-6xl flex-col items-center gap-5 sm:gap-8 md:flex-row-reverse">
		<img src="/images/portions.webp" loading="lazy" decoding="async" alt="" class="po-img h-36 w-36 flex-shrink-0 rounded-3xl object-cover shadow-2xl shadow-black/50 sm:h-56 sm:w-56 md:h-72 md:w-72" />
		<div class="w-full max-w-xl">
			<span class="po-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase sm:mb-3">{d[12].tagline}</span>
			<h2 class="po-ttl mb-4 text-3xl font-bold text-white sm:mb-8 sm:text-4xl md:text-5xl">{d[12].title}</h2>
			<div class="mb-1.5 grid grid-cols-4 gap-1.5 px-2 text-[8px] font-semibold tracking-[0.15em] text-white/25 uppercase sm:mb-2 sm:gap-2 sm:px-3 sm:text-[10px]"><span class="text-left">Grupo</span><span>Carbos</span><span>Proteina</span><span>Grasa</span></div>
			{#each d[12].items as item}
				<div class="po-row mb-1.5 grid grid-cols-4 items-center gap-1.5 rounded-lg border border-white/5 bg-white/[0.03] px-2 py-2 text-xs transition-colors hover:bg-white/[0.05] sm:mb-2 sm:gap-2 sm:px-3 sm:py-3 sm:text-sm">
					<span class="flex items-center gap-1.5 text-left font-medium text-white sm:gap-2"><span class="h-2 w-2 rounded-full sm:h-2.5 sm:w-2.5" style="background:{item.color}"></span>{item.group}</span>
					<span class="text-[#4CAF50]">{item.carbs}</span>
					<span class="text-[#2196F3]">{item.protein}</span>
					<span class="text-[#FF9800]">{item.fat}</span>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- PRACTICE -->
<section id="practice" class="relative flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<div class="pointer-events-none absolute inset-0"><div class="absolute right-1/4 bottom-1/4 h-[500px] w-[500px] rounded-full bg-[#4CAF50]/5 blur-[140px]"></div></div>
	<div class="max-w-5xl text-center">
		<span class="pr-tag mb-2 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase sm:mb-3">{d[13].tagline}</span>
		<h2 class="pr-ttl text-3xl font-bold text-white sm:text-4xl md:text-5xl">{d[13].title}</h2>
		<p class="pr-dsc mx-auto mt-2 max-w-2xl text-sm text-white/40 sm:mt-4 sm:text-base">{d[13].description}</p>
		<div class="mx-auto mt-4 flex w-full max-w-3xl flex-col items-stretch gap-3 sm:mt-8 sm:flex-row sm:gap-5">
			<div class="pr-lb w-full rounded-xl border border-white/10 bg-white/[0.03] p-4 sm:p-6">
				<div class="mb-2 border-b border-white/10 pb-2 sm:mb-3"><h3 class="text-base font-black text-white sm:text-xl">Nutrition Facts</h3><p class="text-[10px] text-white/30 sm:text-xs">{d[13].example.servings} &middot; Serving size {d[13].example.serving}</p></div>
				<div class="flex items-baseline justify-between border-b border-white/10 pb-2"><span class="text-xs font-bold text-white sm:text-sm">Calories</span><span class="text-2xl font-black text-white sm:text-3xl">{d[13].example.calories}</span></div>
				<div class="mt-1.5 space-y-1 text-xs sm:mt-2 sm:space-y-1.5 sm:text-sm">
					<div class="flex justify-between"><span class="text-white/50">Total Fat</span><span class="text-[#FF9800]">{d[13].example.fat}</span></div>
					<div class="flex justify-between"><span class="text-white/50">Total Carbohydrate</span><span class="text-[#4CAF50]">{d[13].example.carbs}</span></div>
					<div class="flex justify-between pl-2 sm:pl-3"><span class="text-[10px] text-white/30 sm:text-xs">Fiber</span><span class="text-[10px] text-white/40 sm:text-xs">{d[13].example.fiber}</span></div>
					<div class="flex justify-between pl-2 sm:pl-3"><span class="text-[10px] text-white/30 sm:text-xs">Added Sugars</span><span class="text-[10px] text-red-400 sm:text-xs">{d[13].example.addedSugars}</span></div>
					<div class="flex justify-between"><span class="text-white/50">Protein</span><span class="text-[#2196F3]">{d[13].example.protein}</span></div>
				</div>
			</div>
			<div class="pr-cl w-full rounded-xl border border-[#4CAF50]/15 bg-[#4CAF50]/5 p-4 text-left sm:p-6">
				<h4 class="mb-2 text-[10px] font-bold tracking-wider text-[#4CAF50] uppercase sm:mb-3 sm:text-xs">Paso a paso</h4>
				<ul class="space-y-1.5 sm:space-y-2.5">
					{#each d[13].example.calculation.steps as step}
						<li class="flex items-start gap-2 text-xs leading-relaxed text-white/50 sm:text-sm"><span class="mt-1 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-[#4CAF50]"></span>{step}</li>
					{/each}
				</ul>
				<div class="mt-3 border-t border-[#4CAF50]/10 pt-2 sm:mt-4 sm:pt-3"><p class="text-xs font-medium text-[#4CAF50] sm:text-sm">{d[13].example.calculation.result}</p></div>
			</div>
		</div>
	</div>
</section>

<!-- CLOSING -->
<section id="closing" class="relative flex h-screen items-center justify-center overflow-hidden px-4 sm:px-6">
	<!-- bg from layout -->
	<div class="pointer-events-none absolute inset-0"><div class="absolute top-1/2 left-1/2 h-[1000px] w-[1000px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-[#4CAF50]/5 blur-[180px]"></div></div>
	<div class="max-w-4xl text-center">
		<img src="/images/logo-sm.webp" alt="Coach BattleBeast" class="cl-logo mx-auto mb-5 h-24 w-auto rounded-xl object-contain sm:mb-8 sm:h-32 md:h-40" />
		<h2 class="cl-ttl text-3xl font-extrabold text-white sm:text-5xl md:text-6xl lg:text-7xl">{d[14].title}</h2>
		<p class="cl-dsc mx-auto mt-4 max-w-2xl text-base leading-relaxed text-white/40 sm:mt-6 sm:text-lg">{d[14].description}</p>
		<p class="cl-hi mx-auto mt-3 max-w-lg text-sm leading-relaxed text-white/50 italic sm:mt-5 sm:text-base">"{d[14].highlight}"</p>
		<p class="cl-cta mt-5 inline-block rounded-xl bg-[#4CAF50]/10 px-6 py-4 text-base font-semibold text-[#4CAF50] sm:mt-8 sm:px-8 sm:py-5 sm:text-lg">{d[14].cta}</p>
		<div class="cl-auth mt-8 flex flex-col items-center gap-1 sm:mt-14"><div class="mb-2 h-px w-12 bg-white/10 sm:mb-3 sm:w-16"></div><span class="text-xs font-semibold tracking-wider text-white/60 uppercase sm:text-sm">{d[14].author}</span><span class="text-[10px] text-white/30 sm:text-xs">{d[14].role}</span></div>
	</div>
</section>
