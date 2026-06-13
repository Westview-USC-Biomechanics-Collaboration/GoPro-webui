<script lang="ts">

    let presets = $state({});

    function openConfirm(){
        (document.getElementById('confirm_modal') as HTMLDialogElement)?.showModal();
    }
    async function openPresets() {
        presets = await getPresets();
        (document.getElementById('preset_modal') as HTMLDialogElement)?.showModal();
    }
    async function clearGopros() {
        try {
            await fetch('http://localhost:8000/controls/clear_gopros');
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }
    async function setKeepAlive() {
        try {
            await fetch('http://localhost:8000/controls/set_keep_alive');
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }
    async function getPresets() {
        try {
            let response = await fetch('http://localhost:8000/controls/get_presets');
            response = await response.json()
            response = response["presets"];
            console.log(response);
            return response;
        } catch (err) {
            console.error('Failed to fetch status:', err);
            return;
        }
    }

</script>

<div class="p-4 rounded-box shadow-sm bg-base-200">
    <h1 class="text-2xl m-2 font-bold text-content">Extra Controls</h1>
    <div class="grid gap-2 grid-cols-2 sm:grid-cols-3">
        <button class="btn btn-block" onclick={openConfirm}>
            Clear GoPro
        </button>
        <button class="btn btn-block" onclick={setKeepAlive}>
            Keep Alive
        </button>
        <button class="btn btn-block" onclick={openPresets}>
            Get Presets
        </button>
    </div>
</div>

<!-- Dialogs -->

<dialog id="preset_modal" class="modal">
    <div class="modal-box">
        <div class="divider text-lg sm:text-xl font-semibold my-3">Front Gopro</div>
        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Recording FPS</div>
                <div class="stat-value text-lg">{#if presets?.front_gopro}{presets.front_gopro["fps"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Lens Mode</div>
                <div class="stat-value text-lg">{#if presets?.front_gopro}{presets.front_gopro["lens_mode"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Resolution</div>
                <div class="stat-value text-lg">{#if presets?.front_gopro}{presets.front_gopro["resolution"]}{/if}</div>
            </div>
        </div>
                <div class="divider text-lg sm:text-xl font-semibold my-3">Top Gopro</div>
        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Recording FPS</div>
                <div class="stat-value text-lg">{#if presets?.top_gopro}{presets.top_gopro["fps"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Lens Mode</div>
                <div class="stat-value text-lg">{#if presets?.top_gopro}{presets.top_gopro["lens_mode"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Resolution</div>
                <div class="stat-value text-lg">{#if presets?.top_gopro}{presets.top_gopro["resolution"]}{/if}</div>
            </div>
        </div>
        <div class="divider text-lg sm:text-xl font-semibold my-3">Short Gopro</div>
        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Recording FPS</div>
                <div class="stat-value text-lg">{#if presets?.short_gopro}{presets.short_gopro["fps"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Lens Mode</div>
                <div class="stat-value text-lg">{#if presets?.short_gopro}{presets.short_gopro["lens_mode"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Resolution</div>
                <div class="stat-value text-lg">{#if presets?.short_gopro}{presets.short_gopro["resolution"]}{/if}</div>
            </div>
        </div>

        <form method="dialog" class="m-4">
            <button class="btn">Close</button>
        </form>
    </div>
</dialog>

<dialog id="confirm_modal" class="modal">
    <div class="modal-box">
        <h1 class="text-xl sm:text-2xl font-bold">Clear Gopros?</h1>
        <p class="text-md sm:text-lg">Would you like to clear to GoPros?</p>
        <div class="modal-action">
            <form onsubmit={
                ()=>{
                    clearGopros();
                    (document.getElementById('confirm_modal') as HTMLDialogElement)?.close();
                }
            }>
                <button class="btn btn-block btn-error w-full">Clear</button>
            </form>
            <form method="dialog">
                <button class="btn">Close</button>
            </form>
        </div>
    </div>
</dialog>
