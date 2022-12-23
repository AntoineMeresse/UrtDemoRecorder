<script>
  import { urtPath, demoTypeFilter } from "./urtService";
  import { open } from "@tauri-apps/api/dialog";
  import { DemoFormats } from "./demos/DemoFormats";

  function deletePath() {
    urtPath.set("");
  }

  function selectPath() {
    open({ multiple: false }).then((filepath) => {
      if (filepath && !Array.isArray(filepath)) {
        urtPath.set(filepath);
      }
    });
  }
</script>

<div>
  <p>Game Path</p>
  <input bind:value={$urtPath} disabled />
  {#if $urtPath}
    <button on:click={deletePath}>X</button>
  {:else}
    <button on:click={selectPath}>Select</button>
  {/if}

  <p>Format</p>
  <select bind:value={$demoTypeFilter}>
    {#each DemoFormats as f}
      <option value={f}>{f}</option>
    {/each}
  </select>
</div>

<style>
  input {
    width: 50vw;
  }
</style>
