import setosaImg from "../assets/setosa.jpg";
import versicolorImg from "../assets/versicolor.jpg";
import virginicaImg from "../assets/virginica.jpg";

function ResultCard({ result, loading }) {

  const getImage = () => {
    if (result === "setosa") return setosaImg;
    if (result === "versicolor") return versicolorImg;
    if (result === "virginica") return virginicaImg;
    return null;
  };

  const image = getImage();

  return (
    <div className="bg-white/90 backdrop-blur-xl p-6 rounded-2xl shadow-2xl flex flex-col items-center justify-center">

      <h2 className="text-xl font-bold text-gray-700 mb-4">
        Prediction Result
      </h2>

      {loading ? (
        <p className="text-purple-600 animate-pulse">Predicting...</p>
      ) : result ? (
        <div className="text-center">

          {image && (
            <img
              src={image}
              alt={result}
              className="w-40 h-40 object-cover rounded-xl shadow-md mb-4"
            />
          )}

          <p className="text-2xl font-bold text-green-600">
            {result}
          </p>

        </div>
      ) : (
        <p className="text-gray-400">
          Enter values and click predict
        </p>
      )}

    </div>
  );
}

export default ResultCard;