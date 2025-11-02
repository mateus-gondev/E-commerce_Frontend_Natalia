<template>
    <div class="adm-layout">
        <AdmNavbar />
        <main class="adm-content">
            <AdmPedidos />
        </main>
    </div>
</template>

<script>
import AdmNavbar from "../../components/Adm/AdmNavbar.vue"
import AdmPedidos from "../../components/Adm/AdmPedidos.vue"

export default {
    name: "Adm",
    components: {
        AdmNavbar,
        AdmPedidos
    }
}

</script>

<style scoped>
.adm-layout {
    display: flex;
}

.adm-content {
    flex: 1;
    margin-left: 280px;
    padding: 2rem;
}
</style>