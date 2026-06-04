import { useState } from "react";

function App() {
  const [value, setValue] = useState("")

  const [isPalindrome, setIsPalindrome] = useState(false)

  const checkIsPalindrome = () => {
    const word1 = value.toLocaleLowerCase().replaceAll(" ",'')
    const word2 = value.split("").reverse().join("").toLocaleLowerCase().replaceAll(" ",'')

    if(word1===word2){
      setIsPalindrome(true)
    }
    else{
      setIsPalindrome(false)
    }
  }
  return (
    <>
    <div>
      <input value={value} onChange={(event)=>{
        setValue(event.target.value)
      }}/>
      <button onClick={checkIsPalindrome}>Проверить</button>
    </div>
    
    
    <div>
      {
        isPalindrome ? 'Палиндром' : 'Не палиндром'
      }
    </div>
    </>
  );
}

export default App;
