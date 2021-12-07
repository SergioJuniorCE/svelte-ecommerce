<script>
	import { page } from '$app/stores';
	import Carousel from '../components/Carousel.svelte';
	import ProductThumbnail from '../components/ProductThumbnail.svelte';

	let images = [
		{ src: 'https://picsum.photos/1100/500?random', alt: 'Random image 1' },
		{ src: 'https://picsum.photos/1100/500?random', alt: 'Random image 2' },
		{ src: 'https://picsum.photos/1100/500?random', alt: 'Random image 3' }
	];

	let ordenamientos = [
		{ label: 'Más vendidos', value: 0 },
		{ label: 'Alphabeticamente A-Z', value: 1 },
		{ label: 'Alphabeticamente Z-A', value: 2 },
		{ label: 'Menor precio', value: 3 },
		{ label: 'Mayor precio', value: 4 }
	];
	let active_order = $page.query.get('order') || 0;

  let products = [
    {
      name: 'Producto 1',
      price: '$100',
      image: 'https://picsum.photos/360?random',
    }
  ];
</script>
<!-- <Carousel images={images}/> -->

<br />
<div class="text-center">
	<h2 class="title my-5">Productos nuevos</h2>
	<div class="row">
		<div class="col-8 text-start">
			<div class="dropdown">
				<button
					class="btn btn-secondary dropdown-toggle"
					type="button"
					id="ordenar-por"
					data-bs-toggle="dropdown"
					aria-expanded="false"
				>
					{ordenamientos[active_order].label}
				</button>
				<ul class="dropdown-menu" aria-labelledby="ordenar-por">
					{#each ordenamientos as ordenamiento}
						<li>
							<a class="dropdown-item" href="?order={ordenamiento.value}">{ordenamiento.label}</a>
						</li>
					{/each}
				</ul>
			</div>
		</div>
		<div class="col-4 text-end">2</div>
	</div>
	<div class="row">
		<div class="col">
			<ProductThumbnail />
		</div>
		<div class="col">
			<ProductThumbnail />
		</div>
		<div class="col">
			<ProductThumbnail />
		</div>
	</div>
</div>

<style>
</style>
