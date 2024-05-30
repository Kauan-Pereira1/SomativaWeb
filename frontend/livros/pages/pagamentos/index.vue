<script>
definePageMeta({
    middleware: 'auth'
})
export default {
    data() {
        return {
            selectedMethod: '', // Método de pagamento selecionado
            paymentMethods: [
                { label: 'Dinheiro', value: 'dinheiro' },
                { label: 'Boleto Bancário', value: 'boleto' },
                { label: 'Pix', value: 'pix' },
                { label: 'Cartão de Crédito', value: 'cartaoCredito' },
                { label: 'Cartão de Débito', value: 'cartaoDebito' }
            ]
        };
    }
};
</script>

<template>
    <main class="home-container flex flex-column align-items-center">
        <div class="payment-container">
            <div class="card">
                <h2>Escolha o Método de Pagamento</h2>
                <div class="payment-methods">
                    <label v-for="(method, index) in paymentMethods" :key="index">
                        <input type="radio" v-model="selectedMethod" :value="method.value">
                        <span class="method-option">{{ method.label }}</span>
                    </label>
                </div>

                <div v-if="selectedMethod === 'dinheiro'" class="payment-details">
                    <h3>Pagamento em Dinheiro</h3>
                    <p>Por favor, efetue o pagamento em dinheiro na entrega.</p>
                </div>

                <div v-if="selectedMethod === 'boleto'" class="payment-details">
                    <h3>Pagamento com Boleto Bancário</h3>
                    <!-- Formulário para gerar o boleto -->
                </div>

                <div v-if="selectedMethod === 'pix'" class="payment-details">
                    <h3>Pagamento com Pix</h3>
                    <!-- Detalhes para pagamento via Pix -->
                </div>

                <div v-if="selectedMethod === 'cartaoCredito'" class="payment-details">
                    <h3>Pagamento com Cartão de Crédito</h3>
                    <!-- Formulário para pagamento com cartão de crédito -->
                </div>

                <div v-if="selectedMethod === 'cartaoDebito'" class="payment-details">
                    <h3>Pagamento com Cartão de Débito</h3>
                    <!-- Formulário para pagamento com cartão de débito -->
                </div>
            </div>
        </div>
    </main>
</template>

<style scoped>
.home-container {
    margin: 0;
    width: 100vw;
    min-height: calc(100vh - 80px);
    background-image: url("nota.jpg");
    background-repeat: repeat;
    background-size: cover;


}

.payment-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.card {
    max-width: 400px;
    padding: 20px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.payment-methods {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
}

.method-option {
    margin-left: 5px;
}

.payment-details {
    border-top: 1px solid #ccc;
    padding-top: 20px;
    margin-top: 20px;
}
</style>