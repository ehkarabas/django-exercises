import axios from "axios";
import { useEffect, useState } from "react";

const EditTutorial = ({ getTutorials, editItem }) => {
  const { id, title: newTitle, description: newDescription } = editItem;

  const [title, setTitle] = useState(newTitle);
  const [description, setDescription] = useState(newDescription);

  //? https://reactjs.org/docs/hooks-reference.html#usestate
  //! State degiskeninin degeri, 1.render ile initialState
  //! parametresinin ilk degerini alir. Dolayisiyle bu durumda
  //! prop'tan gelen ilk deger state'e aktarilir.
  //! Sonradan degisen props degerleri useState'e aktarilmaz.
  //! Eger props'tan gelen degerleri her degisimde useState'e
  //! aktarmak istersek useEffect hook'unu componentDidUpdate
  //! gibi kullanabiriz.

  // ? Parent'taki setEditItem fonksiyonu senkron olarak çalişir ve state'i hemen günceller. Ancak, state'in güncellenmesi ve sonrasinda gerçekleşen yeniden render işlemi asenkron olarak gerçekleşir. Yani, setEditItem fonksiyonu çağrildiktan hemen sonra state'in güncellendiğini varsayamayiz. Bu, React'in state güncellemelerini optimize etmek için kullandiği bir yöntemdir. Yani state degisikligi yeniden render'i tetikler ama yeniden render esnasinda aslinda state yeni halini almamistir, bu nedenle bazi element'ler render edilirken state yeni halini almamis olabilir ama mutlaka render islemi tamamlandiginda yeni halini almis olacaktir. React'ta state güncellemeleri asenkron olduğu için, bir state'i güncelledikten hemen sonra yeni değerine erişmek genellikle beklenildiği gibi çalişmaz. React, performansi optimize etmek için birden fazla state güncellemesini bir arada toplayabilir. Bir state güncellemesi tetiklendiğinde, React bu güncellemeyi bir "iş" olarak siraya alir ve bu işi bir sonraki render döngüsünde işler. Bu nedenle, bir state güncellemesi çağrildiğinda, yeni state değeri hemen mevcut olmayabilir. Bu yüzden, örneğin bir state'i güncelledikten sonra o state'in yeni değerine ihtiyaç duyuyorsaniz, genellikle en iyi yaklaşim useEffect hookunu kullanmaktir. Bu hook, belirli bir state değiştiğinde çalişir, böylece state'in yeni değerini güvende kullanabilirsiniz.

  // ? Eğer bir parent state'i bir child component'e prop olarak geçiyorsak ve child component içinde bu state'i bir elementte doğrudan göstermek istiyorsak (örneğin bir <p> etiketi içinde), genellikle bu durumda undefined durumu ile karşılaşmayız. Çünkü React, parent component'teki state değiştiğinde, bu state'i prop olarak alan child component'i otomatik olarak yeniden render eder ve yeni state değeri ile günceller. Fakat buradaki durum biraz daha karmaşıktır. Burada, child component içinde bir başka state (title ve description), parent'tan gelen prop'lara (newTitle ve newDescription) bağlıdır. Parent'tan gelen prop'lar ilk render sırasında undefined olduğunda, bu değerler child component'teki ilgili state'lere atanır ve bu state'ler de undefined olur. Sonrasında parent'tan prop'lar geldiğinde, bu prop'lar child component'te doğrudan kullanılabileceği bir yerde (örneğin bir <p> etiketi içinde) kullanılsaydı, bu prop'lar otomatik olarak güncellenecekti. Fakat burada bu prop'lar başka bir state'i beslemek için kullanıldığından ve useState hook'unu bir kez çalıştıktan sonra prop'lardaki değişiklikleri otomatik olarak takip etmediğinden (çünkü useState hook'u state'i sadece ilk oluşturulduğunda initialize eder), burada useEffect hook'unu kullanmamız gerekiyor. useEffect hook'u, parent'tan gelen prop'lardaki değişiklikleri takip eder ve bu prop'lar değiştiğinde, ilgili state'leri (title ve description) günceller. Bu sayede, prop'lardaki değişiklikler child component'teki ilgili state'lere yansıtılır.

  //? componentDidUpdate
  //? newTitle veya description her degistiginde local title ve
  //? description state'lerimizi gunceliyoruz.
  useEffect(() => {
    setTitle(newTitle);
    setDescription(newDescription);
  }, [newTitle, newDescription]);

  //! Update (PUT:Whole Update,PATCH :Partially Update)
  const editTutorial = async (id, tutor) => {
    const url = "http://127.0.0.1:8000/tutorials";
    try {
      await axios.put(`${url}/${id}/`, tutor);
    } catch (error) {
      console.log(error);
    }
    getTutorials();
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // ! ES6 sonrasi, object literal'de key olarak variable girildiginde variable name'i key, variable value'yu da value olarak alip object olusturur.
    editTutorial(id, { title, description });
    setTitle("");
    setDescription("");
  };

  return (
    <div>
      <div className="modal fade" id="edit-tutor" tabIndex={-1}>
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h1 className="modal-title fs-5" id="exampleModalLabel">
                Edit Tutorial
              </h1>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              />
            </div>
            <div className="modal-body">
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="title" className="form-label">
                    Title
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="title"
                    placeholder="Enter your title"
                    value={title || ""}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="desc" className="form-label">
                    Description
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="desc"
                    placeholder="Enter your Description"
                    value={description || ""}
                    onChange={(e) => setDescription(e.target.value)}
                    required
                  />
                </div>
              </form>
            </div>
            <div className="modal-footer">
              {/* <button
                type="button"
                className="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button> */}
              <button
                type="button"
                className="btn btn-primary"
                data-bs-dismiss="modal"
                onClick={handleSubmit}
              >
                Save
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EditTutorial;
