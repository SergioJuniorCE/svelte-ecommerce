<script>
	export let images;
</script>

<div id="carousel" class="carousel slide" data-bs-ride="carousel">
	<div class="carousel-indicators">
		{#each images as image, i}
			<button
				type="button"
				data-bs-target="#carousel"
				data-bs-slide-to={i}
				class="active"
				aria-current="true"
				aria-label="Slide {i + 1}"
			/>
		{/each}
	</div>
	<div class="carousel-inner">
		{#each images as image, i}
			<div class="carousel-item {i === 0 ? 'active' : ''}">
				<img src={image.src} class="w-100" alt={image.alt} />
			</div>
		{/each}
	</div>
	<button
		class="carousel-control-prev"
		type="button"
		data-bs-target="#carousel"
		data-bs-slide="prev"
	>
		<span class="carousel-control-prev-icon" aria-hidden="true" />
		<span class="visually-hidden">Previous</span>
	</button>
	<button
		class="carousel-control-next"
		type="button"
		data-bs-target="#carousel"
		data-bs-slide="next"
	>
		<span class="carousel-control-next-icon" aria-hidden="true" />
		<span class="visually-hidden">Next</span>
	</button>
</div>
