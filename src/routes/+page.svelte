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
			t.from('.cb-tag', { autoAlpha: 0, y: 40 }, 0)
			 .from('.cb-ttl', { autoAlpha: 0, y: 80, duration: 0.6 }, 0.1)
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
<section id="hero" class="relative flex h-screen flex-col items-center justify-center overflow-hidden px-6">
	<!-- global bg from css -->
	<div class="pointer-events-none absolute inset-0"><div class="absolute top-1/4 left-1/2 h-[800px] w-[800px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-[#4CAF50]/10 blur-[160px]"></div></div>
	<img src="/images/logo-sm.png" alt="Coach BattleBeast" class="hero-logo mb-6 h-40 w-auto rounded-2xl object-contain sm:h-52" />
	<span class="hero-badge mb-6 rounded-full border border-white/10 bg-white/5 px-6 py-2.5 text-sm font-medium tracking-[0.2em] text-[#81C784] uppercase">{d[0].badge}</span>
	<h1 class="hero-title max-w-5xl text-center text-5xl leading-[1.05] font-extrabold tracking-tight text-white sm:text-7xl md:text-8xl lg:text-9xl">
		{#each d[0].title.split(' ') as w}<span class="word inline-block">{w}&nbsp;</span>{/each}
	</h1>
	<p class="hero-sub mt-8 max-w-xl text-center text-xl leading-relaxed text-white/40">{d[0].subtitle}</p>
	<div class="hero-scroll mt-16 flex flex-col items-center gap-2 text-white/20"><span class="text-[10px] tracking-[0.3em] uppercase">Scroll</span><svg class="h-5 w-5 animate-bounce" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19 14l-7 7m0 0l-7-7m7 7V3"/></svg></div>
</section>

<!-- PROBLEM -->
<section id="problem" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="flex max-w-6xl flex-col items-center gap-10 md:flex-row">
		<img src="/images/problem.jpg" alt="" class="p-img h-64 w-64 flex-shrink-0 rounded-3xl object-cover shadow-2xl shadow-black/50 sm:h-80 sm:w-80" />
		<div class="text-center md:text-left">
			<span class="p-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase">{d[1].tagline}</span>
			<h2 class="p-ttl text-4xl font-bold text-white sm:text-5xl md:text-6xl">{d[1].title}</h2>
			<p class="p-dsc mt-5 max-w-lg text-lg leading-relaxed text-white/40">{d[1].description}</p>
			<div class="mt-6 flex flex-wrap gap-2.5 md:justify-start justify-center">
				{#each d[1].badges as b}<span class="p-bdg rounded-full border border-red-500/20 bg-red-500/8 px-4 py-2 text-sm text-red-400/80">{b}</span>{/each}
			</div>
		</div>
	</div>
</section>

<!-- PHILOSOPHY -->
<section id="philosophy" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="flex max-w-6xl flex-col items-center gap-10 md:flex-row-reverse">
		<img src="/images/philosophy.jpg" alt="" class="ph-img h-64 w-64 flex-shrink-0 rounded-3xl object-cover shadow-2xl shadow-black/50 sm:h-80 sm:w-80" />
		<div class="text-center md:text-left">
			<span class="ph-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase">{d[2].tagline}</span>
			<h2 class="ph-ttl text-4xl font-bold text-white sm:text-5xl md:text-6xl">{d[2].title}</h2>
			<p class="ph-dsc mt-4 max-w-lg text-lg leading-relaxed text-white/40">{d[2].description}</p>
			<p class="ph-hi mt-4 rounded-xl border border-[#4CAF50]/10 bg-[#4CAF50]/5 px-5 py-4 text-sm leading-relaxed text-[#81C784]">{d[2].highlight}</p>
			<div class="mt-8 flex items-center gap-8 md:justify-start justify-center">
				<div class="ph-l flex flex-col items-center"><span class="text-5xl font-black text-[#4CAF50] sm:text-6xl">80%</span><span class="text-xs text-white/30 uppercase">Nutritivo</span></div>
				<div class="h-14 w-px bg-white/10"></div>
				<div class="ph-r flex flex-col items-center"><span class="text-5xl font-black text-[#FF9800] sm:text-6xl">20%</span><span class="text-xs text-white/30 uppercase">Flexible</span></div>
			</div>
		</div>
	</div>
</section>

<!-- TWO KEYS -->
<section id="twokeys" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="max-w-4xl text-center">
		<span class="tk-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase">{d[3].tagline}</span>
		<h2 class="tk-ttl mb-12 text-4xl font-bold text-white sm:text-5xl md:text-6xl">{d[3].title}</h2>
		<div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
			{#each d[3].items as item}
				<div class="tk-card rounded-2xl border border-white/5 bg-white/[0.03] p-8 text-left">
					<span class="mb-3 block text-5xl font-black text-[#4CAF50]/25">{item.number}</span>
					<h3 class="text-xl font-semibold text-white">{item.name}</h3>
					<p class="mt-2 text-base leading-relaxed text-white/40">{item.detail}</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- INGREDIENTS -->
<section id="ingredients" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="flex max-w-6xl flex-col items-center gap-8 md:flex-row">
		<div class="flex flex-shrink-0 flex-col items-center">
			<div class="in-step mb-4 flex h-20 w-20 items-center justify-center rounded-2xl border border-[#4CAF50]/20 bg-[#4CAF50]/8 text-3xl font-black text-[#4CAF50]">01</div>
			<img src="/images/ingredients.jpg" alt="" class="in-img h-52 w-52 rounded-3xl object-cover shadow-2xl shadow-black/50 sm:h-72 sm:w-72" />
		</div>
		<div class="text-center md:text-left">
			<h2 class="in-ttl text-4xl font-bold text-white sm:text-5xl">{d[4].title}</h2>
			<p class="in-dsc mt-4 max-w-lg text-base leading-relaxed text-white/40">{d[4].description}</p>
			<div class="mt-6 flex flex-col gap-3">
				{#each d[4].rules as rule, i}
					<div class="in-r{i} flex items-start gap-4 rounded-xl border border-white/5 bg-white/[0.03] p-5 text-left">
						<div class="flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-lg bg-[#4CAF50]/10">
							<svg class="h-4 w-4 text-[#4CAF50]" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
								{#if rule.icon==='arrow-down'}<path stroke-linecap="round" stroke-linejoin="round" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>{:else if rule.icon==='list'}<path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h8m-8 6h16"/>{:else}<path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/>{/if}
							</svg>
						</div>
						<div><h3 class="font-semibold text-white">{rule.name}</h3><p class="mt-1 text-sm leading-relaxed text-white/40">{rule.detail}</p></div>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>

<!-- SUGAR -->
<section id="sugar" class="relative flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="pointer-events-none absolute inset-0"><div class="absolute top-1/2 left-1/2 h-[700px] w-[700px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-red-500/6 blur-[150px]"></div></div>
	<div class="max-w-5xl text-center">
		<span class="su-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-red-400 uppercase">{d[5].tagline}</span>
		<h2 class="su-ttl text-4xl font-bold text-white sm:text-5xl md:text-6xl">{d[5].title}</h2>
		<p class="su-dsc mt-4 max-w-2xl mx-auto text-base text-white/40">{d[5].description}</p>
		<img src="/images/sugar.jpg" alt="" class="su-img mx-auto mt-6 h-40 w-40 rounded-2xl object-cover shadow-2xl shadow-red-900/30 sm:h-48 sm:w-48" />
		<span class="su-cnt mt-4 block text-8xl font-black text-red-400 tabular-nums sm:text-9xl">0</span>
		<span class="text-sm tracking-wider text-white/30 uppercase">{d[5].countLabel}</span>
		<div class="mt-6 flex max-w-2xl mx-auto flex-wrap justify-center gap-2">
			{#each d[5].hiddenNames as n}<span class="su-pill rounded-full border border-red-500/15 bg-red-500/8 px-3 py-1.5 text-xs text-red-400/70">{n}</span>{/each}
		</div>
		<p class="su-fn mt-6 max-w-lg mx-auto text-xs text-white/20 italic leading-relaxed">{d[5].footnote}</p>
	</div>
</section>

<!-- MARKETING -->
<section id="marketing" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="max-w-5xl text-center">
		<span class="mk-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase">{d[6].tagline}</span>
		<h2 class="mk-ttl text-4xl font-bold text-white sm:text-5xl">{d[6].title}</h2>
		<p class="mt-3 text-base text-white/40">{d[6].description}</p>
		<img src="/images/marketing.jpg" alt="" class="mk-img mx-auto mt-6 h-40 w-full max-w-xl rounded-2xl object-cover shadow-2xl shadow-black/50" />
		<div class="mt-8 grid w-full grid-cols-1 gap-4 sm:grid-cols-2">
			{#each d[6].items as item}
				<div class="mk-cd rounded-xl border border-white/5 bg-white/[0.03] p-6 text-left transition-colors hover:border-[#4CAF50]/20 hover:bg-white/[0.05]">
					<span class="mb-2 inline-block rounded-md bg-[#4CAF50]/10 px-3 py-1 text-xs font-bold tracking-wider text-[#4CAF50] uppercase">{item.label}</span>
					<p class="text-sm leading-relaxed text-white/50">{item.truth}</p>
					<p class="mt-2 border-t border-white/5 pt-2 text-xs text-[#FF9800]/50">{item.warning}</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- SODIUM -->
<section id="sodium" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="max-w-3xl text-center">
		<span class="so-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#FF9800] uppercase">{d[7].tagline}</span>
		<h2 class="so-ttl text-4xl font-bold text-white sm:text-5xl md:text-6xl">{d[7].title}</h2>
		<p class="so-dsc mt-4 text-base text-white/40">{d[7].description}</p>
		<div class="mt-10 flex w-full max-w-lg mx-auto flex-col gap-5">
			{#each d[7].levels as lv}
				<div class="so-bar text-left"><div class="mb-1 flex justify-between"><span class="text-sm font-medium text-white/70">{lv.label}</span><span class="text-xs text-white/40">{lv.value}</span></div>
				<div class="h-3 w-full overflow-hidden rounded-full bg-white/5"><div class="so-fill h-full rounded-full" style="background:{lv.color};width:{lv.color==='#4CAF50'?'15%':lv.color==='#81C784'?'30%':lv.color==='#FF9800'?'55%':'80%'}"></div></div></div>
			{/each}
		</div>
		<p class="so-fn mt-6 text-xs text-white/20 italic leading-relaxed">{d[7].footnote}</p>
	</div>
</section>

<!-- CARBS -->
<section id="carbs" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="max-w-3xl text-center">
		<span class="cb-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase">{d[8].tagline}</span>
		<h2 class="cb-ttl text-4xl font-bold text-white sm:text-5xl">{d[8].title}</h2>
		<p class="cb-dsc mt-4 text-base text-white/40">{d[8].description}</p>
		<div class="mt-8 flex w-full flex-col gap-4">
			{#each d[8].subsections as sub, i}
				<div class="cb-b{i} rounded-xl border border-white/5 bg-white/[0.03] p-5 text-left">
					<h3 class="text-base font-semibold text-white">{sub.name}</h3>
					<p class="mt-1.5 text-sm leading-relaxed text-white/40">{sub.detail}</p>
					<div class="mt-3 rounded-lg bg-[#4CAF50]/5 px-4 py-2"><p class="text-sm font-medium text-[#4CAF50]">{sub.rule}</p></div>
					{#if sub.limit}<p class="mt-2 text-xs text-[#FF9800]/50">{sub.limit}</p>{/if}
					{#if sub.tip}<p class="mt-1.5 text-xs text-[#2196F3]/50">Tip: {sub.tip}</p>{/if}
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- FATS -->
<section id="fats" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="max-w-3xl text-center">
		<span class="ft-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#FF9800] uppercase">{d[9].tagline}</span>
		<h2 class="ft-ttl text-4xl font-bold text-white sm:text-5xl">{d[9].title}</h2>
		<p class="ft-dsc mt-4 text-base text-white/40">{d[9].description}</p>
		<div class="mt-8 grid w-full grid-cols-1 gap-4 sm:grid-cols-2">
			<div class="ft-gd rounded-xl border border-[#4CAF50]/10 bg-[#4CAF50]/5 p-5 text-left">
				<h3 class="mb-3 text-xs font-bold tracking-wider text-[#4CAF50] uppercase">Priorizar</h3>
				{#each d[9].good as g}<div class="mb-2 flex items-center gap-2"><div class="h-2 w-2 rounded-full bg-[#4CAF50]"></div><span class="text-sm text-white/60">{g}</span></div>{/each}
			</div>
			<div class="ft-bd rounded-xl border border-red-500/10 bg-red-500/5 p-5 text-left">
				<h3 class="mb-3 text-xs font-bold tracking-wider text-red-400 uppercase">Evitar frecuente</h3>
				{#each d[9].bad as b}<div class="mb-2 flex items-center gap-2"><div class="h-2 w-2 rounded-full bg-red-400"></div><span class="text-sm text-white/60">{b}</span></div>{/each}
			</div>
		</div>
		<div class="mt-5 flex justify-center gap-3">
			{#each d[9].limits as l}<div class="ft-lm rounded-lg border border-white/5 bg-white/[0.03] px-4 py-2.5 text-center"><span class="text-xs font-bold uppercase" style="color:{l.color}">{l.type}</span><p class="mt-0.5 text-xs text-white/40">{l.limit}</p></div>{/each}
		</div>
		<p class="ft-fn mt-5 text-xs text-white/20 italic leading-relaxed">{d[9].footnote}</p>
	</div>
</section>

<!-- CALORIES -->
<section id="calories" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="max-w-3xl text-center">
		<span class="cal-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase">{d[10].tagline}</span>
		<h2 class="cal-ttl text-4xl font-bold text-white sm:text-5xl md:text-7xl">{d[10].title}</h2>
		<p class="cal-dsc mt-6 max-w-xl mx-auto text-xl leading-relaxed text-white/40">{d[10].description}</p>
	</div>
</section>

<!-- MACROS -->
<section id="macros" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="flex max-w-6xl flex-col items-center gap-8 md:flex-row">
		<img src="/images/macros.jpg" alt="" class="ma-img h-60 w-60 flex-shrink-0 rounded-3xl object-cover shadow-2xl shadow-black/50 sm:h-80 sm:w-80" />
		<div class="text-center md:text-left">
			<span class="ma-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase">{d[11].tagline}</span>
			<h2 class="ma-ttl text-4xl font-bold text-white sm:text-5xl">{d[11].title}</h2>
			<p class="ma-dsc mt-4 max-w-lg text-base leading-relaxed text-white/40">{d[11].description}</p>
			<p class="ma-dt mt-4 max-w-lg text-sm leading-relaxed text-white/30">{d[11].detail}</p>
			<div class="ma-ex mt-4 rounded-xl border border-white/5 bg-white/[0.03] px-5 py-4"><p class="text-sm leading-relaxed text-white/50">{d[11].example}</p></div>
		</div>
	</div>
</section>

<!-- PORTIONS -->
<section id="portions" class="flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="flex max-w-6xl flex-col items-center gap-8 md:flex-row-reverse">
		<img src="/images/portions.jpg" alt="" class="po-img h-56 w-56 flex-shrink-0 rounded-3xl object-cover shadow-2xl shadow-black/50 sm:h-72 sm:w-72" />
		<div class="w-full max-w-xl">
			<span class="po-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase">{d[12].tagline}</span>
			<h2 class="po-ttl mb-8 text-4xl font-bold text-white sm:text-5xl">{d[12].title}</h2>
			<div class="mb-2 grid grid-cols-4 gap-2 px-3 text-[10px] font-semibold tracking-[0.15em] text-white/25 uppercase"><span class="text-left">Grupo</span><span>Carbos</span><span>Proteina</span><span>Grasa</span></div>
			{#each d[12].items as item}
				<div class="po-row mb-2 grid grid-cols-4 items-center gap-2 rounded-lg border border-white/5 bg-white/[0.03] px-3 py-3 text-sm transition-colors hover:bg-white/[0.05]">
					<span class="flex items-center gap-2 text-left font-medium text-white"><span class="h-2.5 w-2.5 rounded-full" style="background:{item.color}"></span>{item.group}</span>
					<span class="text-[#4CAF50]">{item.carbs}</span>
					<span class="text-[#2196F3]">{item.protein}</span>
					<span class="text-[#FF9800]">{item.fat}</span>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- PRACTICE -->
<section id="practice" class="relative flex h-screen items-center justify-center overflow-hidden px-6">
	<div class="pointer-events-none absolute inset-0"><div class="absolute right-1/4 bottom-1/4 h-[500px] w-[500px] rounded-full bg-[#4CAF50]/5 blur-[140px]"></div></div>
	<div class="max-w-5xl text-center">
		<span class="pr-tag mb-3 inline-block text-xs font-semibold tracking-[0.3em] text-[#4CAF50] uppercase">{d[13].tagline}</span>
		<h2 class="pr-ttl text-4xl font-bold text-white sm:text-5xl">{d[13].title}</h2>
		<p class="pr-dsc mt-4 max-w-2xl mx-auto text-base text-white/40">{d[13].description}</p>
		<div class="mt-8 flex w-full max-w-3xl mx-auto flex-col items-stretch gap-5 sm:flex-row">
			<div class="pr-lb w-full rounded-xl border border-white/10 bg-white/[0.03] p-6">
				<div class="mb-3 border-b border-white/10 pb-2"><h3 class="text-xl font-black text-white">Nutrition Facts</h3><p class="text-xs text-white/30">{d[13].example.servings} &middot; Serving size {d[13].example.serving}</p></div>
				<div class="flex items-baseline justify-between border-b border-white/10 pb-2"><span class="text-sm font-bold text-white">Calories</span><span class="text-3xl font-black text-white">{d[13].example.calories}</span></div>
				<div class="mt-2 space-y-1.5 text-sm">
					<div class="flex justify-between"><span class="text-white/50">Total Fat</span><span class="text-[#FF9800]">{d[13].example.fat}</span></div>
					<div class="flex justify-between"><span class="text-white/50">Total Carbohydrate</span><span class="text-[#4CAF50]">{d[13].example.carbs}</span></div>
					<div class="flex justify-between pl-3"><span class="text-xs text-white/30">Fiber</span><span class="text-xs text-white/40">{d[13].example.fiber}</span></div>
					<div class="flex justify-between pl-3"><span class="text-xs text-white/30">Added Sugars</span><span class="text-xs text-red-400">{d[13].example.addedSugars}</span></div>
					<div class="flex justify-between"><span class="text-white/50">Protein</span><span class="text-[#2196F3]">{d[13].example.protein}</span></div>
				</div>
			</div>
			<div class="pr-cl w-full rounded-xl border border-[#4CAF50]/15 bg-[#4CAF50]/5 p-6 text-left">
				<h4 class="mb-3 text-xs font-bold tracking-wider text-[#4CAF50] uppercase">Paso a paso</h4>
				<ul class="space-y-2.5">
					{#each d[13].example.calculation.steps as step}
						<li class="flex items-start gap-2 text-sm leading-relaxed text-white/50"><span class="mt-1 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-[#4CAF50]"></span>{step}</li>
					{/each}
				</ul>
				<div class="mt-4 border-t border-[#4CAF50]/10 pt-3"><p class="text-sm font-medium text-[#4CAF50]">{d[13].example.calculation.result}</p></div>
			</div>
		</div>
	</div>
</section>

<!-- CLOSING -->
<section id="closing" class="relative flex h-screen items-center justify-center overflow-hidden px-6">
	<!-- bg from layout -->
	<div class="pointer-events-none absolute inset-0"><div class="absolute top-1/2 left-1/2 h-[1000px] w-[1000px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-[#4CAF50]/5 blur-[180px]"></div></div>
	<div class="max-w-4xl text-center">
		<img src="/images/logo-sm.png" alt="Coach BattleBeast" class="cl-logo mx-auto mb-8 h-32 w-auto rounded-xl object-contain sm:h-40" />
		<h2 class="cl-ttl text-5xl font-extrabold text-white sm:text-6xl md:text-7xl">{d[14].title}</h2>
		<p class="cl-dsc mt-6 max-w-2xl mx-auto text-lg leading-relaxed text-white/40">{d[14].description}</p>
		<p class="cl-hi mt-5 max-w-lg mx-auto text-base leading-relaxed text-white/50 italic">"{d[14].highlight}"</p>
		<p class="cl-cta mt-8 inline-block rounded-xl bg-[#4CAF50]/10 px-8 py-5 text-lg font-semibold text-[#4CAF50]">{d[14].cta}</p>
		<div class="cl-auth mt-14 flex flex-col items-center gap-1"><div class="mb-3 h-px w-16 bg-white/10"></div><span class="text-sm font-semibold tracking-wider text-white/60 uppercase">{d[14].author}</span><span class="text-xs text-white/30">{d[14].role}</span></div>
	</div>
</section>
