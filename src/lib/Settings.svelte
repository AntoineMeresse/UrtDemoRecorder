<script>
  import { urtPath } from "./urtService";
  import { open } from "@tauri-apps/api/dialog";

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
  {#if $urtPath.length !== 0}
    <button on:click={deletePath}>X</button>
  {:else}
    <button on:click={selectPath}>Select</button>
  {/if}
</div>

<style>
  input {
    width: 50vw;
  }
</style>
