<template>
    <transition name="slide-cart">
        <div v-if="carrinhoAberto" class="cart-slider bg-white shadow position-fixed"
            style="top: 0; right: 0; height: 100vh; width: 350px; z-index: 1100;">
            <div class="d-flex justify-content-between align-items-center p-3 border-bottom">
                <h5 class="mb-0">
                    <i class="fas fa-gem me-2"></i> Carrinho de Joias
                </h5>
                <button class="btn btn-sm btn-outline-secondary" @click="fecharCarrinho" title="Fechar">
                    &times;
                </button>
            </div>

            <div class="p-3 text-center text-muted" style="height: calc(100vh - 150px);">
                <i class="fas fa-box-open fa-3x mb-3"></i>
                <p>Seu carrinho está vazio</p>
            </div>

            <div class="p-3 border-top">
                <button class="btn btn-success w-100" disabled>
                    Finalizar Compra
                </button>
            </div>
        </div>
    </transition>
</template>

<script>
export default {
    name: "CarrinhoLateral",
    data() {
        return {
            carrinhoAberto: false,
        };
    },
    methods: {
        abrirCarrinho() {
            this.carrinhoAberto = true;
        },
        fecharCarrinho() {
            this.carrinhoAberto = false;
        },
    },
};
</script>

<style scoped>
/* Animação de transição lateral */
.slide-cart-enter-active,
.slide-cart-leave-active {
    transition: transform 0.4s ease;
}

.slide-cart-enter-from,
.slide-cart-leave-to {
    transform: translateX(100%);
}

.slide-cart-enter-to,
.slide-cart-leave-from {
    transform: translateX(0);
}
</style>
