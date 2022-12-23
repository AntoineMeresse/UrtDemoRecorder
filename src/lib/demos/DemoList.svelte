<script lang="ts">
  import { demoList, loadDemosFiles } from "$lib/urtService";
  import { onMount } from "svelte";
  import Demo from "./Demo.svelte";

  let errorMessage = "";

  onMount(() => {
    loadDemosFiles();
  });
</script>

<div>
  {#each $demoList as demo}
    <Demo demoName={demo} />
  {/each}
</div>
<p>{errorMessage}</p>
