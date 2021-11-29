<script>
	import { goto } from '$app/navigation';

	export let product;

	function onClick() {
		goto(`/collections/${category}/${id}`);
	}
</script>

<div class="mx-3 py-2 text-center" on:click={onClick}>
	<img src="http://localhost:1337{product.images[0].url}" alt="{product.title} image" style="max-width: 300px; aspect-ratio: 1 / 1"/>
	<div class="text-center">
		<h5 class="bold mt-1">{product.title}</h5>
		<p class="bold my-0">${product.price}</p>
	</div>
</div>

<style>
	.bold {
		font-weight: bold;
	}
</style>
