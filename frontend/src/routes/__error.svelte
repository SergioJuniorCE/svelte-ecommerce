<script context="module">
	/** @type {import('@sveltejs/kit').ErrorLoad} */
	export function load({ error, status }) {
		return {
			props: {
				status: status,
				message: error.message
			}
		};
	}
</script>

<script>
	export let status;
	export let message;
</script>

<div class="container mt-5">
	<div class="error mx-auto" data-text={status}>
		<p class="m-0">{status}</p>
	</div>
	<div class="text-center" style="color: black">
		<!-- Only for debug -->
		<p>[{message}]</p>
		<p>Parece que encontraste un error en la matrix...</p>
		<a
			href="/"
			class="link">⬅️ Regresa al menu principal</a
		>
	</div>
</div>

<style>
	*,
	*::before,
	*::after {
		box-sizing: border-box;
	}
	.error {
		color: #5a5c69;
		font-size: 7rem;
		position: relative;
		line-height: 1;
		width: 12.5rem;
	}
	.error:before {
		content: attr(data-text);
		position: absolute;
		left: -2px;
		text-shadow: 1px 0 #4e73df;
		top: 0;
		color: #5a5c69;
		background: #f8f9fc;
		overflow: hidden;
		clip: rect(0, 900px, 0, 0);
		animation: noise-anim-2 3s infinite linear alternate-reverse;
	}

	.error:after {
		content: attr(data-text);
		position: absolute;
		left: 2px;
		text-shadow: -1px 0 #e74a3b;
		top: 0;
		color: #5a5c69;
		background: #f8f9fc;
		overflow: hidden;
		clip: rect(0, 900px, 0, 0);
		animation: noise-anim 2s infinite linear alternate-reverse;
	}
	@-webkit-keyframes noise-anim {
		0% {
			clip: rect(60px, 9999px, 4px, 0);
		}
		5% {
			clip: rect(36px, 9999px, 84px, 0);
		}
		10% {
			clip: rect(14px, 9999px, 45px, 0);
		}
		15% {
			clip: rect(63px, 9999px, 52px, 0);
		}
		20% {
			clip: rect(41px, 9999px, 64px, 0);
		}
		25% {
			clip: rect(73px, 9999px, 78px, 0);
		}
		30% {
			clip: rect(85px, 9999px, 60px, 0);
		}
		35% {
			clip: rect(68px, 9999px, 77px, 0);
		}
		40% {
			clip: rect(16px, 9999px, 55px, 0);
		}
		45% {
			clip: rect(70px, 9999px, 96px, 0);
		}
		50% {
			clip: rect(19px, 9999px, 48px, 0);
		}
		55% {
			clip: rect(24px, 9999px, 65px, 0);
		}
		60% {
			clip: rect(65px, 9999px, 90px, 0);
		}
		65% {
			clip: rect(91px, 9999px, 5px, 0);
		}
		70% {
			clip: rect(11px, 9999px, 41px, 0);
		}
		75% {
			clip: rect(79px, 9999px, 48px, 0);
		}
		80% {
			clip: rect(62px, 9999px, 63px, 0);
		}
		85% {
			clip: rect(88px, 9999px, 97px, 0);
		}
		90% {
			clip: rect(22px, 9999px, 39px, 0);
		}
		95% {
			clip: rect(1px, 9999px, 71px, 0);
		}
		100% {
			clip: rect(67px, 9999px, 70px, 0);
		}
	}
	@keyframes noise-anim {
		0% {
			clip: rect(60px, 9999px, 4px, 0);
		}
		5% {
			clip: rect(36px, 9999px, 84px, 0);
		}
		10% {
			clip: rect(14px, 9999px, 45px, 0);
		}
		15% {
			clip: rect(63px, 9999px, 52px, 0);
		}
		20% {
			clip: rect(41px, 9999px, 64px, 0);
		}
		25% {
			clip: rect(73px, 9999px, 78px, 0);
		}
		30% {
			clip: rect(85px, 9999px, 60px, 0);
		}
		35% {
			clip: rect(68px, 9999px, 77px, 0);
		}
		40% {
			clip: rect(16px, 9999px, 55px, 0);
		}
		45% {
			clip: rect(70px, 9999px, 96px, 0);
		}
		50% {
			clip: rect(19px, 9999px, 48px, 0);
		}
		55% {
			clip: rect(24px, 9999px, 65px, 0);
		}
		60% {
			clip: rect(65px, 9999px, 90px, 0);
		}
		65% {
			clip: rect(91px, 9999px, 5px, 0);
		}
		70% {
			clip: rect(11px, 9999px, 41px, 0);
		}
		75% {
			clip: rect(79px, 9999px, 48px, 0);
		}
		80% {
			clip: rect(62px, 9999px, 63px, 0);
		}
		85% {
			clip: rect(88px, 9999px, 97px, 0);
		}
		90% {
			clip: rect(22px, 9999px, 39px, 0);
		}
		95% {
			clip: rect(1px, 9999px, 71px, 0);
		}
		100% {
			clip: rect(67px, 9999px, 70px, 0);
		}
	}
	@-webkit-keyframes noise-anim-2 {
		0% {
			clip: rect(38px, 9999px, 29px, 0);
		}
		5% {
			clip: rect(2px, 9999px, 55px, 0);
		}
		10% {
			clip: rect(29px, 9999px, 96px, 0);
		}
		15% {
			clip: rect(9px, 9999px, 43px, 0);
		}
		20% {
			clip: rect(13px, 9999px, 64px, 0);
		}
		25% {
			clip: rect(16px, 9999px, 93px, 0);
		}
		30% {
			clip: rect(28px, 9999px, 31px, 0);
		}
		35% {
			clip: rect(25px, 9999px, 24px, 0);
		}
		40% {
			clip: rect(83px, 9999px, 42px, 0);
		}
		45% {
			clip: rect(88px, 9999px, 17px, 0);
		}
		50% {
			clip: rect(88px, 9999px, 49px, 0);
		}
		55% {
			clip: rect(40px, 9999px, 28px, 0);
		}
		60% {
			clip: rect(79px, 9999px, 89px, 0);
		}
		65% {
			clip: rect(39px, 9999px, 97px, 0);
		}
		70% {
			clip: rect(93px, 9999px, 75px, 0);
		}
		75% {
			clip: rect(15px, 9999px, 11px, 0);
		}
		80% {
			clip: rect(17px, 9999px, 44px, 0);
		}
		85% {
			clip: rect(97px, 9999px, 97px, 0);
		}
		90% {
			clip: rect(33px, 9999px, 25px, 0);
		}
		95% {
			clip: rect(14px, 9999px, 96px, 0);
		}
		100% {
			clip: rect(59px, 9999px, 95px, 0);
		}
	}
	@keyframes noise-anim-2 {
		0% {
			clip: rect(38px, 9999px, 29px, 0);
		}
		5% {
			clip: rect(2px, 9999px, 55px, 0);
		}
		10% {
			clip: rect(29px, 9999px, 96px, 0);
		}
		15% {
			clip: rect(9px, 9999px, 43px, 0);
		}
		20% {
			clip: rect(13px, 9999px, 64px, 0);
		}
		25% {
			clip: rect(16px, 9999px, 93px, 0);
		}
		30% {
			clip: rect(28px, 9999px, 31px, 0);
		}
		35% {
			clip: rect(25px, 9999px, 24px, 0);
		}
		40% {
			clip: rect(83px, 9999px, 42px, 0);
		}
		45% {
			clip: rect(88px, 9999px, 17px, 0);
		}
		50% {
			clip: rect(88px, 9999px, 49px, 0);
		}
		55% {
			clip: rect(40px, 9999px, 28px, 0);
		}
		60% {
			clip: rect(79px, 9999px, 89px, 0);
		}
		65% {
			clip: rect(39px, 9999px, 97px, 0);
		}
		70% {
			clip: rect(93px, 9999px, 75px, 0);
		}
		75% {
			clip: rect(15px, 9999px, 11px, 0);
		}
		80% {
			clip: rect(17px, 9999px, 44px, 0);
		}
		85% {
			clip: rect(97px, 9999px, 97px, 0);
		}
		90% {
			clip: rect(33px, 9999px, 25px, 0);
		}
		95% {
			clip: rect(14px, 9999px, 96px, 0);
		}
		100% {
			clip: rect(59px, 9999px, 95px, 0);
		}
	}
</style>
