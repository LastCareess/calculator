import { useState } from "react"

function App() {
  const [frstNum, setFrstNum] = useState("")
  const [scndNum, setScndNum] = useState("")

  const [operation, setOperation] = useState("+")
  
  const result = (frstNum !== "" && scndNum !=="")
    ? eval(`${parseInt(frstNum)}${operation}${parseInt(scndNum)}`)
    : 0
  return (
    <>
    <div>
      <input value={frstNum} type="number" placeholder="Введите первое число" onChange={(event)=>{
        setFrstNum(event.target.value)
      }}/>
      
      <select value={operation} onChange={(event)=>{setOperation(event.target.value)}}>
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
      </select>

      <input value={scndNum} type="number" placeholder="Введите второе число" onChange={(event)=>{
        setScndNum(event.target.value)
      }}/>
    </div>

    <div>
      {result}
    </div>
    </>
  );
}

export default App;
