<template>
    <transition name="slide-cart">
        <div
            v-if="carrinhoAberto"
            class="cart-slider bg-white shadow position-fixed"
            style="top: 0; right: 0; height: 100vh; width: 350px; z-index: 1100;"
        >
            <!-- HEADER -->
            <div class="d-flex justify-content-between align-items-center p-3 border-bottom">
                <h5 class="mb-0">
                    <i class="fas fa-gem me-2"></i> Carrinho
                </h5>
                <button class="btn btn-sm btn-outline-secondary" @click="fecharCarrinho">
                    &times;
                </button>
            </div>

            <!-- LISTA DE PRODUTOS -->
            <div class="p-3" style="height: calc(100vh - 150px); overflow-y: auto;">
                <div v-if="cart.length === 0" class="text-center text-muted mt-5">
                    <i class="fas fa-box-open fa-3x mb-3"></i>
                    <p>Seu carrinho está vazio</p>
                </div>

                <div
                    v-for="item in cart"
                    :key="item.id"
                    class="d-flex align-items-center mb-3 pb-2 border-bottom"
                >
                    <img
                        :src="item.img"
                        alt="produto"
                        class="rounded me-2"
                        style="width: 60px; height: 60px; object-fit: cover;"
                    />

                    <div class="flex-grow-1">
                        <h6 class="mb-1">{{ item.title }}</h6>
                        <p class="mb-1 text-muted">{{ item.preco }}</p>

                        <!-- QUANTIDADE -->
                        <div class="d-flex align-items-center">
                            <button class="btn btn-sm btn-outline-secondary" @click="diminuir(item.id)">
                                -
                            </button>
                            <span class="mx-2">{{ item.quantity }}</span>
                            <button class="btn btn-sm btn-outline-secondary" @click="aumentar(item.id)">
                                +
                            </button>
                        </div>
                    </div>

                    <!-- REMOVER -->
                    <button class="btn btn-sm btn-danger ms-2" @click="remover(item.id)">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            </div>

            <!-- FOOTER TOTAL -->
            <div class="p-3 border-top">
                <h5 class="mb-3">Total: <strong>{{ totalFormatado }}</strong></h5>

                <button
                    class="btn btn-success w-100"
                    :disabled="cart.length === 0"
                >
                    Finalizar Compra
                </button>
            </div>
        </div>
    </transition>
</template>

<script>
import cartStore from "@/services/cart";

export default {
    name: "CarrinhoLateral",

    data() {
        return {
            carrinhoAberto: false,
            cart: [],
        };
    },

    computed: {
        total() {
            return this.cart.reduce((acc, item) => {
                const preco = Number(item.preco.replace("R$", "").replace(",", "."));
                return acc + preco * item.quantity;
            }, 0);
        },

        totalFormatado() {
            return this.total.toLocaleString("pt-BR", {
                style: "currency",
                currency: "BRL",
            });
        },
    },

    methods: {
        abrirCarrinho() {
            this.carrinhoAberto = true;
            this.carregarCarrinho();
        },

        fecharCarrinho() {
            this.carrinhoAberto = false;
        },

        carregarCarrinho() {
            this.cart = cartStore.getCart();
        },

        remover(id) {
            cartStore.remove(id);
            this.carregarCarrinho();
        },

        aumentar(id) {
            const item = this.cart.find(i => i.id === id);
            cartStore.changeQuantity(id, item.quantity + 1);
            this.carregarCarrinho();
        },

        diminuir(id) {
            const item = this.cart.find(i => i.id === id);
            if (item.quantity > 1) {
                cartStore.changeQuantity(id, item.quantity - 1);
                this.carregarCarrinho();
            }
        },
    },

    mounted() {
        // Atualiza carrinho quando um produto é adicionado
        window.addEventListener("cart-updated", this.carregarCarrinho);

        // Permite abrir carrinho via evento global
        window.addEventListener("open-cart", this.abrirCarrinho);

        this.carregarCarrinho();
    },

    beforeUnmount() {
        window.removeEventListener("cart-updated", this.carregarCarrinho);
        window.removeEventListener("open-cart", this.abrirCarrinho);
    }
};
</script>

<style scoped>
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
