<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';

	export let title;
	export let href;

	function goTo() {
		goto(href, {
			replaceState: true
		});
	}
</script>

<li class="nav-item">
	<a
		class="nav-link"
		class:active={$page.path === `/${href}`}
		aria-current="page"
		href="{href}"
	>
		{title}</a
	>
</li>
