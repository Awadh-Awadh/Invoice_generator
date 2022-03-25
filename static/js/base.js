btn1 = document.getElementById("btn")
btn2 = document.getElementById("add")

function button_onclick() {
  document.getElementById("btn").style.visibility="hidden";
 }
print_btn = document.getElementById("printBtn")
console.log(print_btn)

print_btn.addEventListener("click", ()=>{
  btn1.remove()
  btn2.remove()
  print_btn.remove()
  window.print()
  
  
 

})
