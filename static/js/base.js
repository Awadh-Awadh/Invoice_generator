btn = document.getElementById("btn")

function button_onclick() {
  document.getElementById("btn").style.visibility="hidden";
 }
print_btn = document.getElementById("printBtn")
console.log(print_btn)

print_btn.addEventListener("click", ()=>{
  window.print()
})
