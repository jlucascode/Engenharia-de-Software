const output = document.getElementById('output');

function write(...args){
	const line = args.map(a => {
		if (typeof a === 'object') return JSON.stringify(a, null, 2);
		return String(a);
	}).join(' ');
	output.textContent += line + '\n';
}

function clearOutput(){
	output.textContent = '';
}

// aula: variáveis, tipos e operadores
function runExamples(){
	clearOutput();
	write('Exemplo: console-like output (esboço para atividade)');

	
	let nome = 'João Lucas';
	const ano = 2025;
	write('Variáveis:', 'nome =', nome, '| ano =', ano);

	
	const idade = 20;
	const preco = 19.9;
	const ativo = true;
	const lista = [1, 2, 3];
	write('Tipos:', typeof nome, typeof idade, typeof preco, typeof ativo, Array.isArray(lista) ? 'array' : typeof lista);

	
	const soma = 2 + 3;
	const comparacao = idade > 18;
	write('Operadores: 2 + 3 =', soma, '| idade > 18 ?', comparacao);


	function saudacao(u){
		return `Olá, ${u}! Bem-vindo(a).`;
	}
	write(saudacao(nome));

	// demonstrar objeto
	const pessoa = { nome, idade, anoNascimento: ano - idade };
	write('Objeto pessoa:', pessoa);
}
document.getElementById('run-examples').addEventListener('click', runExamples);
document.getElementById('clear-output').addEventListener('click', clearOutput);
