<script>
  import { goto } from "$app/navigation"

	export let category;
	$: image = category.image.formats.small;
  $: alt = category.image.alternativeText;
  $: name = category.title.toLowerCase();
</script>

<a href="/collections/{name}">
  <div class="text-center">
    <img src="http://localhost:1337{image.url}" alt="{alt}" style="max-width: 300; max-height: 300;"/>
    <p style="text-decoration: underline;">{category.title}</p>
  </div>
</a>
