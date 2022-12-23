import { writable, type Writable } from "svelte/store";

export const urtPath : Writable<string> = writable("");
export const demoList : Writable<string[]> = writable([]);
export const demoFilter : Writable<string> = writable("")

export function removeExecFromPath(execpath : string) : string{
    const pathSplit = execpath.split('\\');
    const path = pathSplit.slice(0,-1).join('\\')
    console.log(path);
    return path;
}

export function getDemosFolder(urtPath : string) : string {
    return removeExecFromPath(urtPath) + "\\q3ut4\\demos";
}