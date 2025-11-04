<template>
  <div class="min-h-screen flex items-center justify-center bg-[#287BFF]">
    <div class="bg-white rounded-xl shadow-xl w-full max-w-md p-8 text-center">
      <!-- Logo e título -->
      <div class="mb-6">
        <div class="flex flex-col items-center">
          <div class="text-3xl font-semibold text-gray-800 tracking-wide">BLUASSIST</div>
          <div class="h-1 w-10 bg-[#287BFF] rounded-full mt-2"></div>
        </div>
      </div>

      <!-- Texto principal -->
      <h2 class="text-2xl font-bold text-gray-900 mb-4">Redefina sua senha</h2>

      <!-- Texto explicativo -->
      <p class="text-gray-600 text-sm mb-8 text-left">
        <span class="font-semibold text-gray-800">Hey Jack,</span><br><br>
        Precisa redefinir sua senha? Sem problemas! Basta clicar no botão abaixo e pronto.
Se você não fez esta solicitação, ignore este e-mail..
      </p>

      <!-- Botão -->
      <button
        class="bg-[#287BFF] hover:bg-[#1f66d1] text-white font-medium py-3 px-6 rounded-md w-full transition-colors"
      >
        Redefina sua senha
      </button>
    </div>
  </div>
</template>

<script>
    export default {
        name: "RedSenha",
    };


</script>

<style scoped>
/* Arredondamento dos cantos e sombra suave já feitos via Tailwind */
</style>