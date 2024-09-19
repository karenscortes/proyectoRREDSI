<template>
    <!-- Capa que cubre toda la pantalla cuando loading está activo -->
    <div v-if="loading" class="spinner-overlay">
        <div class="loader">Loading...</div>
    </div>
</template>

<script>
import { computed } from 'vue';
import { useSpinnerStore } from "@/store/spinner";

export default {
    setup() {
        const spinnerStore = useSpinnerStore();
        return {
            loading: computed(() => spinnerStore.loading),
        };
    },
};
</script>

<style scoped>
.spinner-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
}

.loader, .loader:before, .loader:after {
    border-radius: 50%;
    width: 2.5em;
    height: 2.5em;
    animation-fill-mode: both;
    animation: bblFadInOut 1.8s infinite ease-in-out;
}

.loader {
    color: rgb(255,183,6);
    font-size: 7px;
    position: relative;
    text-indent: -9999em;
    transform: translateZ(0);
    animation-delay: -0.16s;
}

.loader:before, .loader:after {
    content: '';
    position: absolute;
    top: 0;
}

.loader:before {
    left: -3.5em;
    animation-delay: -0.32s;
}

.loader:after {
    left: 3.5em;
}

@keyframes bblFadInOut {
    0%, 80%, 100% {
        box-shadow: 0 2.5em 0 -1.3em;
    }
    40% {
        box-shadow: 0 2.5em 0 0;
    }
}
</style>
