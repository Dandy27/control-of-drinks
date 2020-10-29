import 'dart:io';

main(){

  print('Tequila: ');
  var peso_liquido = stdin.readLineSync();
  var peso_liquidoN = double.parse(peso_liquido);

  print('Quantidade de doses');
  var quant_doses = stdin.readLineSync();
  var quant_dosesN = double.parse(quant_doses);

  print('Peso bruto da garrafa');
  var peso_bruto = stdin.readLineSync();
  var peso_brutoN = double.parse(peso_bruto);

  print('tara');
  var tara = stdin.readLineSync();
  var taraN = double.parse(tara);

  print('garrafa aberta bar');
  var grf_aberta = stdin.readLineSync();
  var grf_abertaN = double.parse(grf_aberta);

  print('Quantidade de doses: ');
  var total = (grf_abertaN - taraN) * quant_dosesN / (peso_brutoN - taraN); 

  print(total);


}