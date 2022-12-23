<script lang="ts">
  import { demoList, loadDemosFiles, demoListSelected } from "$lib/urtService";
  import { onMount } from "svelte";
  import Demo from "./Demo.svelte";

  let errorMessage = "";

  onMount(() => {
    loadDemosFiles();
  });
</script>

<p>Selected list : {$demoListSelected}</p>
<div>
  {#each $demoList as demo (demo)}
    <Demo demoName={demo} />
  {/each}
</div>
<p>{errorMessage}</p>
