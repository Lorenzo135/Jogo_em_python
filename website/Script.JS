function mouseFora(imagem) {
   const originalSrc = imagem.getAttribute("data-original"); //Essa linha busca o valor que está no data-original da tag img do html: Exemplo "minecraft.webp"
   if (originalSrc) {
       imagem.src = originalSrc;
   }
}

function mouseEmCima(imagem) {
   const hoverSrc = imagem.getAttribute("data-hover");//Essa linha busca o valor que está no data-hover da tag img do html: Exemplo "mine_2.jpg"
   if (hoverSrc) {
       imagem.src = hoverSrc;
   }
}