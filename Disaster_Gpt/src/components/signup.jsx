
function Signup() {   

    const handleSubmit=(e)=>{
        e.preventDefault();
        const first=e.target.fname.value;
        const last=e.target.lname.value;
        const location= e.target.location.value;
        const phoneNumber= e.target.pNumber.value;
        var obj = {
            FirstName: first,
            LastName: last,
            Location: location,
            PhoneNumber: phoneNumber,
        };
        fetch("/application",{
            method: 'POST',
            Headers:{
                "Content-type":"Sign-Up"
            },
            body:JSON.stringify(obj)
        });
      }
      
    return (
      <div className="min-h-screen py-40">
        <div className="container mx-auto">
          <div className="flex flex-col lg:flex-row w-10/12 lg:w-8/12 bg-[#27282a] rounded-xl mx-auto shadow-lg overflow-hidden max-sm:mb-0 max-sm:w-1/2 max-sm:content-center">
            {/* Left section */}
            <div
              className="w-full lg:w-1/2 flex flex-col items-center justify-center p-12 bg-no-repeat bg-cover bg-center"
              style={{ backgroundImage: "url('images/Register-Background.png')" }}
            >
              <h1 className="text-white text-3xl mb-3">Welcome</h1>
              <div>
                <p className="text-white">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean suspendisse aliquam varius rutrum purus maecenas ac{' '}
                  <br></br>
                  <a href="#" className="flex text-white justify-center hover:text-purple-500 font-semibold">Learn more</a>
                </p>
              </div>
            </div>
  
            {/* Right section */}
            <div className="w-full lg:w-1/2 py-16 px-12">
              <h2 className="text-3xl mb-4 text-white max-sm:mt-0">Register</h2>
              <p className="mb-4 text-white">Create your account. It’s free and only takes a minute</p>
              <form onSubmit={handleSubmit} >
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
                  <input type="text" name ="fname" placeholder="Firstname" className="border border-gray-400 py-1 px-2" />
                  <input type="text" name ="lname"  placeholder="Surname" className="border border-gray-400 py-1 px-2" />
                </div>
  
                <div className="mt-5">
                  <input type="text" pattern="[A-Za-z]\d[A-Za-z]\d[A-Za-z]\d" name="location" placeholder="Location" className="border border-gray-400 py-1 px-2 w-full" />
                </div>
                <div className="mt-5">
                  <input type="text" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" name ="pNumber" placeholder="Phone Number" className="border border-gray-400 py-1 px-2 w-full" />
                </div>
                <div className="mt-5">
                <button 
                type="submit" 
                className="w-full hover:text-purple-500 text-gray-400 bg-white py-3 text-center text-grey-400"
                >
                Register Now
                </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    );
  }
  
  export default Signup;
  