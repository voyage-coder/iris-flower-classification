import { useState } from "react";
import InputCard from "./components/InputCard";
import ResultCard from "./components/ResultCard";

function App() {
  const [formData, setFormData] = useState({
    sepal_length: "",
    sepal_width: "",
    petal_length: "",
    petal_width: "",
  });

  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handlePredict = () => {
    const isValid =
      formData.sepal_length &&
      formData.sepal_width &&
      formData.petal_length &&
      formData.petal_width;

    if (!isValid) {
      alert("Please fill all fields");
      return;
    }

    setLoading(true);
    setResult("");

    fetch(`${import.meta.env.VITE_API_URL}/predict`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        sepal_length: parseFloat(formData.sepal_length),
        sepal_width: parseFloat(formData.sepal_width),
        petal_length: parseFloat(formData.petal_length),
        petal_width: parseFloat(formData.petal_width),
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        setResult(data.prediction);
        setLoading(false);
      })
      .catch(() => {
        setResult("Server Error ❌");
        setLoading(false);
      });
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500 p-6">

      <div className="w-full max-w-4xl grid md:grid-cols-2 gap-6">

        <InputCard
          formData={formData}
          handleChange={handleChange}
          handlePredict={handlePredict}
          loading={loading}
        />

        <ResultCard result={result} loading={loading} />

      </div>
    </div>
  );
}

export default App;