<script>
  import { demoFilter, loadDemosFiles } from "$lib/urtService";

  function resetFilter() {
    demoFilter.set("");
  }
</script>

<input bind:value={$demoFilter} placeholder="Demo name" />
{#if $demoFilter}
  <button on:click={resetFilter}>X</button>
{/if}
<button on:click={loadDemosFiles}>♻️</button>
