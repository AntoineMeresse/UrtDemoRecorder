<script>
  import DemoFilter from "./demos/DemoFilter.svelte";
  import DemoList from "./demos/DemoList.svelte";
  import { urtPath } from "./urtService";
</script>

<div>
  {#if $urtPath}
    <DemoFilter />
    <DemoList />
  {:else}
    <p>Please go in the settings and add your game path</p>
  {/if}
</div>
