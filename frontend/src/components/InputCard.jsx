function InputCard({ formData, handleChange, handlePredict, loading }) {
  return (
    <div className="bg-white/90 backdrop-blur-xl p-6 rounded-2xl shadow-2xl">

      <h1 className="text-2xl font-bold mb-4 text-gray-800">
        🌸 Iris Predictor
      </h1>

      <div className="space-y-3">

        <input
          name="sepal_length"
          value={formData.sepal_length}
          onChange={handleChange}
          placeholder="Sepal Length"
          className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
        />

        <input
          name="sepal_width"
          value={formData.sepal_width}
          onChange={handleChange}
          placeholder="Sepal Width"
          className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
        />

        <input
          name="petal_length"
          value={formData.petal_length}
          onChange={handleChange}
          placeholder="Petal Length"
          className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
        />

        <input
          name="petal_width"
          value={formData.petal_width}
          onChange={handleChange}
          placeholder="Petal Width"
          className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
        />

      </div>

      <button
        onClick={handlePredict}
        disabled={loading}
        className="w-full mt-5 bg-purple-600 text-white py-3 rounded-xl hover:bg-purple-700 transition font-semibold"
      >
        {loading ? "Predicting..." : "Predict"}
      </button>

    </div>
  );
}

export default InputCard;