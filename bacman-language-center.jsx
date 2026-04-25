import React, { useState } from 'react';
import {
  Menu,
  X,
  GraduationCap,
  Users,
  Star,
  Clock,
  BookOpen,
  Phone,
  Mail,
  MapPin,
  ChevronLeft,
  ChevronRight,
  MessageCircle,
  Globe,
  Award,
  Target,
} from 'lucide-react';

export default function CohassetLanguageCenter() {
  const [currentPage, setCurrentPage] = useState('inicio');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [courseFilter, setCourseFilter] = useState('Todos');
  const [testimonialIndex, setTestimonialIndex] = useState(0);
  const [formData, setFormData] = useState({ name: '', email: '', message: '' });
  const [formSubmitted, setFormSubmitted] = useState(false);

  // Courses data
  const coursesData = [
    {
      id: 1,
      title: 'English Basics',
      level: 'Principiante',
      description: 'Aprende los fundamentos del inglés desde cero.',
      duration: '12 semanas',
      price: '$299',
    },
    {
      id: 2,
      title: 'Conversational English',
      level: 'Intermedio',
      description: 'Domina conversaciones cotidianas con confianza.',
      duration: '10 semanas',
      price: '$349',
    },
    {
      id: 3,
      title: 'Business English',
      level: 'Especializado',
      description: 'Inglés profesional para el mundo empresarial.',
      duration: '8 semanas',
      price: '$399',
    },
    {
      id: 4,
      title: 'Advanced Grammar',
      level: 'Avanzado',
      description: 'Domina la gramática avanzada del inglés.',
      duration: '10 semanas',
      price: '$379',
    },
    {
      id: 5,
      title: 'IELTS Preparation',
      level: 'Especializado',
      description: 'Prepárate para el examen IELTS con expertos.',
      duration: '14 semanas',
      price: '$449',
    },
    {
      id: 6,
      title: 'Kids English',
      level: 'Principiante',
      description: 'Inglés divertido para niños de 5-10 años.',
      duration: '16 semanas',
      price: '$249',
    },
  ];

  // Testimonials
  const testimonials = [
    {
      name: 'María García',
      text: 'Increíble experiencia. Los profesores son muy dedicados y el aprendizaje es muy efectivo.',
      role: 'Estudiante de Business English',
    },
    {
      name: 'Carlos López',
      text: 'Pasé mi examen de IELTS con la ayuda de COHASSET. Altamente recomendado.',
      role: 'Certificación IELTS',
    },
    {
      name: 'Ana Martínez',
      text: 'Las clases son interactivas y motivadoras. Me siento muy cómoda aprendiendo aquí.',
      role: 'Estudiante de Conversational English',
    },
  ];

  // Filter courses
  const filteredCourses = coursesData.filter(
    (course) => courseFilter === 'Todos' || course.level === courseFilter
  );

  // Handle form submission
  const handleFormSubmit = (e) => {
    e.preventDefault();
    if (formData.name && formData.email && formData.message) {
      setFormSubmitted(true);
      setFormData({ name: '', email: '', message: '' });
      setTimeout(() => setFormSubmitted(false), 3000);
    }
  };

  // Render page content
  const renderPage = () => {
    switch (currentPage) {
      case 'inicio':
        return renderInicio();
      case 'cursos':
        return renderCursos();
      case 'nosotros':
        return renderNosotros();
      case 'contacto':
        return renderContacto();
      default:
        return renderInicio();
    }
  };

  // INICIO PAGE
  const renderInicio = () => (
    <div className="min-h-screen">
      {/* Hero Section */}
      <div
        className="min-h-[600px] flex items-center justify-center text-center px-4 py-20 relative overflow-hidden"
        style={{
          background: 'linear-gradient(135deg, #FDDBB5 0%, #EDF3EC 100%)',
        }}
      >
        <div className="absolute top-0 right-0 w-96 h-96 rounded-full opacity-20" style={{ background: '#F4A261' }}></div>
        <div className="absolute bottom-0 left-0 w-72 h-72 rounded-full opacity-20" style={{ background: '#8BA888' }}></div>

        <div className="relative z-10 max-w-2xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6" style={{ color: '#2D3436' }}>
            Domina el Inglés, Conquista el Mundo
          </h1>
          <p className="text-lg md:text-xl mb-8" style={{ color: '#636E72' }}>
            Aprende inglés con métodos innovadores y profesores certificados. Tu camino hacia la fluencia comienza aquí.
          </p>
          <button
            onClick={() => setCurrentPage('cursos')}
            className="px-8 py-3 text-white font-semibold rounded-lg transition-all hover:scale-105 active:scale-95"
            style={{ background: '#F4A261' }}
          >
            Explorar Cursos
          </button>
        </div>
      </div>

      {/* Stats Section */}
      <div className="py-16 px-4" style={{ background: '#FFF5EB' }}>
        <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="text-center">
            <Users className="w-12 h-12 mx-auto mb-4" style={{ color: '#F4A261' }} />
            <p className="text-3xl font-bold" style={{ color: '#2D3436' }}>500+</p>
            <p style={{ color: '#636E72' }}>Estudiantes Activos</p>
          </div>
          <div className="text-center">
            <BookOpen className="w-12 h-12 mx-auto mb-4" style={{ color: '#8BA888' }} />
            <p className="text-3xl font-bold" style={{ color: '#2D3436' }}>15+</p>
            <p style={{ color: '#636E72' }}>Cursos Disponibles</p>
          </div>
          <div className="text-center">
            <Star className="w-12 h-12 mx-auto mb-4" style={{ color: '#F4A261' }} />
            <p className="text-3xl font-bold" style={{ color: '#2D3436' }}>98%</p>
            <p style={{ color: '#636E72' }}>Satisfacción</p>
          </div>
        </div>
      </div>

      {/* Featured Courses */}
      <div className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-16" style={{ color: '#2D3436' }}>
            Cursos Destacados
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {coursesData.slice(0, 3).map((course) => (
              <div
                key={course.id}
                className="rounded-xl p-6 transition-all hover:shadow-xl hover:scale-105 cursor-pointer"
                style={{ background: '#FFF5EB', border: '2px solid #FDDBB5' }}
              >
                <div className="flex items-center justify-between mb-4">
                  <span
                    className="text-sm font-semibold px-3 py-1 rounded-full"
                    style={{ background: '#EDF3EC', color: '#8BA888' }}
                  >
                    {course.level}
                  </span>
                  <GraduationCap style={{ color: '#F4A261' }} />
                </div>
                <h3 className="text-xl font-bold mb-3" style={{ color: '#2D3436' }}>
                  {course.title}
                </h3>
                <p className="mb-4" style={{ color: '#636E72' }}>
                  {course.description}
                </p>
                <div className="flex items-center gap-4 text-sm mb-4" style={{ color: '#636E72' }}>
                  <span className="flex items-center gap-1">
                    <Clock className="w-4 h-4" /> {course.duration}
                  </span>
                </div>
                <button
                  className="w-full py-2 text-white font-semibold rounded-lg transition-all hover:opacity-90"
                  style={{ background: '#8BA888' }}
                >
                  Más Información
                </button>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Why Choose Us */}
      <div
        className="py-20 px-4"
        style={{ background: '#EDF3EC' }}
      >
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-16" style={{ color: '#2D3436' }}>
            ¿Por qué elegirnos?
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div className="text-center">
              <Award className="w-12 h-12 mx-auto mb-4" style={{ color: '#F4A261' }} />
              <h3 className="font-bold mb-2" style={{ color: '#2D3436' }}>Profesores Certificados</h3>
              <p style={{ color: '#636E72' }}>Expertos con años de experiencia en enseñanza.</p>
            </div>
            <div className="text-center">
              <Target className="w-12 h-12 mx-auto mb-4" style={{ color: '#8BA888' }} />
              <h3 className="font-bold mb-2" style={{ color: '#2D3436' }}>Métodos Efectivos</h3>
              <p style={{ color: '#636E72' }}>Enseñanza basada en resultados comprobados.</p>
            </div>
            <div className="text-center">
              <Globe className="w-12 h-12 mx-auto mb-4" style={{ color: '#F4A261' }} />
              <h3 className="font-bold mb-2" style={{ color: '#2D3436' }}>Clases Flexibles</h3>
              <p style={{ color: '#636E72' }}>Online y presencial, adaptados a tu horario.</p>
            </div>
            <div className="text-center">
              <Users className="w-12 h-12 mx-auto mb-4" style={{ color: '#8BA888' }} />
              <h3 className="font-bold mb-2" style={{ color: '#2D3436' }}>Comunidad Activa</h3>
              <p style={{ color: '#636E72' }}>Aprende con compañeros de todo el mundo.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  // CURSOS PAGE
  const renderCursos = () => (
    <div className="min-h-screen py-16 px-4" style={{ background: '#FFF5EB' }}>
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-12" style={{ color: '#2D3436' }}>
          Nuestros Cursos
        </h1>

        {/* Filter Tabs */}
        <div className="flex flex-wrap gap-3 mb-12 pb-6 border-b-2" style={{ borderColor: '#FDDBB5' }}>
          {['Todos', 'Principiante', 'Intermedio', 'Avanzado', 'Especializado'].map((level) => (
            <button
              key={level}
              onClick={() => setCourseFilter(level)}
              className={`px-4 py-2 rounded-lg font-semibold transition-all ${
                courseFilter === level ? 'text-white scale-105' : 'bg-white'
              }`}
              style={{
                background: courseFilter === level ? '#F4A261' : '#FFF5EB',
                color: courseFilter === level ? 'white' : '#636E72',
              }}
            >
              {level}
            </button>
          ))}
        </div>

        {/* Courses Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredCourses.map((course) => (
            <div
              key={course.id}
              className="rounded-xl p-6 shadow-md transition-all hover:shadow-xl hover:-translate-y-2"
              style={{ background: 'white', border: '1px solid #FDDBB5' }}
            >
              <div className="flex items-start justify-between mb-4">
                <span
                  className="text-sm font-semibold px-3 py-1 rounded-full"
                  style={{ background: '#EDF3EC', color: '#8BA888' }}
                >
                  {course.level}
                </span>
              </div>
              <h3 className="text-2xl font-bold mb-3" style={{ color: '#2D3436' }}>
                {course.title}
              </h3>
              <p className="mb-6 leading-relaxed" style={{ color: '#636E72' }}>
                {course.description}
              </p>
              <div className="space-y-3 mb-6">
                <div className="flex items-center gap-2 text-sm" style={{ color: '#636E72' }}>
                  <Clock className="w-4 h-4" style={{ color: '#F4A261' }} />
                  <span>{course.duration}</span>
                </div>
                <div className="flex items-center gap-2 text-sm" style={{ color: '#636E72' }}>
                  <BookOpen className="w-4 h-4" style={{ color: '#8BA888' }} />
                  <span className="text-lg font-bold" style={{ color: '#2D3436' }}>{course.price}</span>
                </div>
              </div>
              <button
                className="w-full py-2 text-white font-semibold rounded-lg transition-all hover:opacity-90"
                style={{ background: '#F4A261' }}
              >
                Inscribirse Ahora
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

  // NOSOTROS PAGE
  const renderNosotros = () => (
    <div className="min-h-screen">
      {/* Mission & Vision */}
      <div className="py-20 px-4" style={{ background: '#EDF3EC' }}>
        <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12">
          <div>
            <h2 className="text-3xl font-bold mb-6" style={{ color: '#2D3436' }}>
              Nuestra Misión
            </h2>
            <p className="text-lg leading-relaxed mb-4" style={{ color: '#636E72' }}>
              En COHASSET Language Center, nos dedicamos a proporcionar educación de calidad en inglés que trascienda las barreras del idioma y abra oportunidades globales para nuestros estudiantes.
            </p>
            <p className="text-lg leading-relaxed" style={{ color: '#636E72' }}>
              Creemos que dominar el inglés es la llave para expandir horizontes personales y profesionales.
            </p>
          </div>
          <div>
            <h2 className="text-3xl font-bold mb-6" style={{ color: '#2D3436' }}>
              Nuestra Visión
            </h2>
            <p className="text-lg leading-relaxed mb-4" style={{ color: '#636E72' }}>
              Ser la academia de inglés más reconocida y confiable de la región, transformando vidas a través de la educación de excelencia.
            </p>
            <p className="text-lg leading-relaxed" style={{ color: '#636E72' }}>
              Aspiramos a crear una comunidad global de aprendices comprometidos con el crecimiento continuo.
            </p>
          </div>
        </div>
      </div>

      {/* Methodology */}
      <div className="py-20 px-4" style={{ background: '#FFF5EB' }}>
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-12 text-center" style={{ color: '#2D3436' }}>
            Nuestra Metodología
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="p-6 rounded-lg" style={{ background: 'white', border: '2px solid #FDDBB5' }}>
              <h3 className="text-xl font-bold mb-4" style={{ color: '#F4A261' }}>Aprendizaje Comunicativo</h3>
              <p style={{ color: '#636E72' }}>
                Enfatizamos la comunicación real desde el primer día, permitiendo que los estudiantes desarrollen confianza hablando.
              </p>
            </div>
            <div className="p-6 rounded-lg" style={{ background: 'white', border: '2px solid #EDF3EC' }}>
              <h3 className="text-xl font-bold mb-4" style={{ color: '#8BA888' }}>Clases Interactivas</h3>
              <p style={{ color: '#636E72' }}>
                Utilizamos actividades dinámicas, juegos y debates para mantener el aprendizaje emocionante y relevante.
              </p>
            </div>
            <div className="p-6 rounded-lg" style={{ background: 'white', border: '2px solid #FDDBB5' }}>
              <h3 className="text-xl font-bold mb-4" style={{ color: '#F4A261' }}>Progreso Personalizado</h3>
              <p style={{ color: '#636E72' }}>
                Cada estudiante sigue su propio ritmo con evaluaciones regulares y retroalimentación constructiva.
              </p>
            </div>
            <div className="p-6 rounded-lg" style={{ background: 'white', border: '2px solid #EDF3EC' }}>
              <h3 className="text-xl font-bold mb-4" style={{ color: '#8BA888' }}>Recursos Modernos</h3>
              <p style={{ color: '#636E72' }}>
                Acceso a plataformas digitales, ejercicios interactivos y materiales multimedia de última generación.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Team */}
      <div className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold mb-12 text-center" style={{ color: '#2D3436' }}>
            Nuestro Equipo
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              { name: 'Emily Johnson', title: 'Directora Académica', specialty: 'English Literature' },
              { name: 'James Wilson', title: 'Profesor Senior', specialty: 'Business English' },
              { name: 'Sofia García', title: 'Coordinadora de Cursos', specialty: 'Conversational Skills' },
            ].map((member, idx) => (
              <div
                key={idx}
                className="text-center p-8 rounded-xl transition-all hover:shadow-lg"
                style={{ background: '#EDF3EC' }}
              >
                <div
                  className="w-24 h-24 rounded-full mx-auto mb-4 flex items-center justify-center"
                  style={{ background: '#FDDBB5' }}
                >
                  <Users className="w-12 h-12" style={{ color: '#F4A261' }} />
                </div>
                <h3 className="text-xl font-bold" style={{ color: '#2D3436' }}>
                  {member.name}
                </h3>
                <p style={{ color: '#F4A261' }} className="font-semibold">
                  {member.title}
                </p>
                <p style={{ color: '#636E72' }} className="text-sm">
                  {member.specialty}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Testimonials Carousel */}
      <div className="py-20 px-4" style={{ background: '#FFF5EB' }}>
        <div className="max-w-2xl mx-auto">
          <h2 className="text-3xl font-bold mb-12 text-center" style={{ color: '#2D3436' }}>
            Lo que dicen nuestros estudiantes
          </h2>
          <div className="p-8 rounded-xl text-center" style={{ background: 'white', border: '2px solid #FDDBB5' }}>
            <p className="text-lg italic mb-6" style={{ color: '#636E72' }}>
              "{testimonials[testimonialIndex].text}"
            </p>
            <p className="font-bold" style={{ color: '#2D3436' }}>
              {testimonials[testimonialIndex].name}
            </p>
            <p style={{ color: '#F4A261' }} className="text-sm">
              {testimonials[testimonialIndex].role}
            </p>
          </div>
          <div className="flex items-center justify-center gap-4 mt-8">
            <button
              onClick={() =>
                setTestimonialIndex(
                  testimonialIndex === 0 ? testimonials.length - 1 : testimonialIndex - 1
                )
              }
              className="p-2 rounded-lg transition-all hover:scale-110"
              style={{ background: '#F4A261', color: 'white' }}
            >
              <ChevronLeft className="w-5 h-5" />
            </button>
            <div className="flex gap-2">
              {testimonials.map((_, idx) => (
                <div
                  key={idx}
                  className="w-2 h-2 rounded-full transition-all"
                  style={{
                    background: idx === testimonialIndex ? '#F4A261' : '#FDDBB5',
                  }}
                ></div>
              ))}
            </div>
            <button
              onClick={() =>
                setTestimonialIndex(
                  testimonialIndex === testimonials.length - 1 ? 0 : testimonialIndex + 1
                )
              }
              className="p-2 rounded-lg transition-all hover:scale-110"
              style={{ background: '#8BA888', color: 'white' }}
            >
              <ChevronRight className="w-5 h-5" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );

  // CONTACTO PAGE
  const renderContacto = () => (
    <div className="min-h-screen py-16 px-4" style={{ background: '#FFF5EB' }}>
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-12" style={{ color: '#2D3436' }}>
          Contacto
        </h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
          {/* Contact Form */}
          <div className="lg:col-span-2">
            <form
              onSubmit={handleFormSubmit}
              className="p-8 rounded-xl"
              style={{ background: 'white', border: '2px solid #FDDBB5' }}
            >
              <h2 className="text-2xl font-bold mb-6" style={{ color: '#2D3436' }}>
                Envíanos tu consulta
              </h2>

              {formSubmitted && (
                <div
                  className="p-4 mb-6 rounded-lg text-white font-semibold"
                  style={{ background: '#8BA888' }}
                >
                  ¡Mensaje enviado! Te contactaremos pronto.
                </div>
              )}

              <div className="mb-6">
                <label className="block font-semibold mb-2" style={{ color: '#2D3436' }}>
                  Nombre
                </label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  className="w-full px-4 py-2 rounded-lg border-2 focus:outline-none"
                  style={{ borderColor: '#FDDBB5', background: '#FFF5EB' }}
                  required
                />
              </div>

              <div className="mb-6">
                <label className="block font-semibold mb-2" style={{ color: '#2D3436' }}>
                  Email
                </label>
                <input
                  type="email"
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  className="w-full px-4 py-2 rounded-lg border-2 focus:outline-none"
                  style={{ borderColor: '#FDDBB5', background: '#FFF5EB' }}
                  required
                />
              </div>

              <div className="mb-6">
                <label className="block font-semibold mb-2" style={{ color: '#2D3436' }}>
                  Mensaje
                </label>
                <textarea
                  value={formData.message}
                  onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                  className="w-full px-4 py-2 rounded-lg border-2 focus:outline-none h-32"
                  style={{ borderColor: '#FDDBB5', background: '#FFF5EB' }}
                  required
                ></textarea>
              </div>

              <button
                type="submit"
                className="w-full py-3 text-white font-semibold rounded-lg transition-all hover:opacity-90"
                style={{ background: '#F4A261' }}
              >
                Enviar Mensaje
              </button>
            </form>
          </div>

          {/* Contact Info */}
          <div>
            <div
              className="p-8 rounded-xl mb-8"
              style={{ background: '#EDF3EC', border: '2px solid #B5C9B3' }}
            >
              <h3 className="text-xl font-bold mb-6" style={{ color: '#2D3436' }}>
                Información de Contacto
              </h3>

              <div className="space-y-6">
                <div className="flex gap-4">
                  <Phone className="w-6 h-6 flex-shrink-0" style={{ color: '#F4A261' }} />
                  <div>
                    <p className="font-semibold" style={{ color: '#2D3436' }}>
                      Teléfono
                    </p>
                    <p style={{ color: '#636E72' }}>+51 1 2345678</p>
                  </div>
                </div>

                <div className="flex gap-4">
                  <Mail className="w-6 h-6 flex-shrink-0" style={{ color: '#8BA888' }} />
                  <div>
                    <p className="font-semibold" style={{ color: '#2D3436' }}>
                      Email
                    </p>
                    <p style={{ color: '#636E72' }}>info@cohassetchr.com</p>
                  </div>
                </div>

                <div className="flex gap-4">
                  <MapPin className="w-6 h-6 flex-shrink-0" style={{ color: '#F4A261' }} />
                  <div>
                    <p className="font-semibold" style={{ color: '#2D3436' }}>
                      Ubicación
                    </p>
                    <p style={{ color: '#636E72' }}>Lima, Perú</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Social Links */}
            <div
              className="p-8 rounded-xl"
              style={{ background: '#FDDBB5' }}
            >
              <h3 className="text-xl font-bold mb-4" style={{ color: '#2D3436' }}>
                Síguenos
              </h3>
              <div className="flex gap-4">
                <a href="#" className="p-3 rounded-lg bg-white transition-all hover:scale-110">
                  <Globe className="w-5 h-5" style={{ color: '#8BA888' }} />
                </a>
                <a href="#" className="p-3 rounded-lg bg-white transition-all hover:scale-110">
                  <MessageCircle className="w-5 h-5" style={{ color: '#F4A261' }} />
                </a>
                <a href="#" className="p-3 rounded-lg bg-white transition-all hover:scale-110">
                  <Users className="w-5 h-5" style={{ color: '#8BA888' }} />
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen flex flex-col" style={{ background: '#FFF5EB' }}>
      {/* Navigation */}
      <nav
        className="sticky top-0 z-50 px-4 py-4 shadow-md"
        style={{ background: 'white' }}
      >
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-3">
            <img
              src="data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgNDAwIDIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAKICAGPGRLZNM+CiAgICAgIDwhLS0gR3JhZGllbnQgZm9yIDNEIGVmZmVjdCBvbiBjaXJjbGVzIC0tPgogICAgICA8cmFkaWFsR3JhZGllbnQgaWQ9ImNpcmNsZUdyYWRpZW50IiBjeD0iMzUlIiBjeT0iMzUlIj4KICAgICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdHlsZT0ic3RvcC1jb2xvcjojM0I4MkY2O3N0b3Atb3BhY2l0eToxIiAvPgogICAgICAgIDxzdG9wIG9mZnNldD0iNzAlIiBzdHlsZT0ic3RvcC1jb2xvcjojMjU2M0VCO3N0b3Atb3BhY2l0eToxIiAvPgogICAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3R5bGU9InN0b3AtY29sb3I6IzFFNDBBRjtzdG9wLW9wYWNpdHk6MSIgLz4KICAgICAgPC9yYWRpYWxHcmFkaWVudD4KCiAgICAgIDwhLS0gU2hhZG93IGZpbHRlciBmb3IgY2lyY2xlcyAtLT4KICAgICAgPGZpbHRlciBpZD0iY2lyY2xlU2hhZG93IiB4PSItNTAlIiB5PSItNTAlIiB3aWR0aD0iMjAwJSIgaGVpZ2h0PSIyMDAlIj4KICAgICAgICA8ZmVEcm9wU2hhZG93IGR4PSIyIiBkeT0iMiIgc3RkRGV2aWF0aW9uPSIxLjUiIGZsb29kLW9wYWNpdHk9IjAuMyIgLz4KICAgICAgPC9maWx0ZXI+CiAgPC9kZWZzPgoKICA8IS0tIFN1bmJ1cnN0IGNpcmNsZSBwYXR0ZXJuIG9uIHRoZSBsZWZ0IC0tPgogIDxnIGlkPSJzdW5idXJzdCI+CiAgICAgIDwhLS0gQ2VudGVyIHBvaW50IGF0IGFwcHJveGltYXRlbHkgeD04MCwgeT0xMDAgLS0+CgogICAgICA8IS0tIFJpZ2h0IHJheSAoMCBkZWdyZWVzKSAtLT4KICAgICAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMiIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgogICAgICA8Y2lyY2xlIGN4PSIxMTUiIGN5PSIxMDAiIHI9IjkiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iMTI4IiBjeT0iMTAwIiByPSI2IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CgogICAgICA8IS0tIFRvcC1yaWdodCByYXkgKDQ1IGRlZ3JlZXMpIC0tPgogICAgICA8Y2lyY2xlIGN4PSI5NS40IiBjeT0iNzkuNiIgcj0iMTEiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iMTA2LjYiIGN5PSI2OC40IiByPSI4IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjExNi41IiBjeT0iNTcuNSIgcj0iNSIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgoKICAgICAgPCEtLSBUb3AgcmF5ICg5MCBkZWdyZWVzKSAtLT4KICAgICAgPGNpcmNsZSBjeD0iODAiIGN5PSI3OCIgcj0iMTEuNSIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgogICAgICA8Y2lyY2xlIGN4PSI4MCIgY3k9IjYzIiByPSI4LjUiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iODAiIGN5PSI1MCIgcj0iNS41IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CgogICAgICA8IS0tIFRvcC1sZWZ0IHJheSAoMTM1IGRlZ3JlZXMpIC0tPgogICAgICA8Y2lyY2xlIGN4PSI2NC42IiBjeT0iNzkuNiIgcj0iMTEiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iNTMuNCIgY3k9IjY4LjQiIHI9IjgiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iNDMuNSIgY3k9IjU3LjUiIHI9IjUiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KCiAgICAgIDwhLS0gTGVmdCByYXkgKDE4MCBkZWdyZWVzKSAtLT4KICAgICAgPGNpcmNsZSBjeD0iNjAiIGN5PSIxMDAiIHI9IjEyIiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjQ1IiBjeT0iMTAwIiByPSI5IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjMyIiBjeT0iMTAwIiByPSI2IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CgogICAgICA8IS0tIEJvdHRvbS1sZWZ0IHJheSAoMjI1IGRlZ3JlZXMpIC0tPgogICAgICA8Y2lyY2xlIGN4PSI2NC42IiBjeT0iMTIwLjQiIHI9IjExIiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjUzLjQiIGN5PSIxMzEuNiIgcj0iOCIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgogICAgICA8Y2lyY2xlIGN4PSI0My41IiBjeT0iMTQyLjUiIHI9IjUiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KCiAgICAgIDwhLS0gQm90dG9tIHJheSAoMjcwIGRlZ3JlZXMpIC0tPgogICAgICA8Y2lyY2xlIGN4PSI4MCIgY3k9IjEyMiIgcj0iMTEuNSIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgogICAgICA8Y2lyY2xlIGN4PSI4MCIgY3k9IjEzNyIgcj0iOC41IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjgwIiBjeT0iMTUwIiByPSI1LjUiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KCiAgICAgIDwhLS0gQm90dG9tLXJpZ2h0IHJheSAoMzE1IGRlZ3JlZXMpIC0tPgogICAgICA8Y2lyY2xlIGN4PSI5NS40IiBjeT0iMTIwLjQiIHI9IjExIiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjEwNi42IiBjeT0iMTMxLjYiIHI9IjgiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iMTE2LjUiIGN5PSIxNDIuNSIgcj0iNSIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgoKICAgICAgPCEtLSBMYXJnZSBjZW50cmFsIGNpcmNsZSAtLT4KICAgICAgPGNpcmNsZSBjeD0iODAiIGN5PSIxMDAiIHI9IjE0IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgPC9nPgogIAogIDwhLS0gVGV4dCBvbiB0aGUgcmlnaHQgLS0+CiAgPGcgaWQ9InRleHQiPgogICAgPCEtLSBDT0hBU1NFVCB3aXRoIHVuZGVybGluZXMgLS0+CiAgICA8dGV4dCB4PSIxNTUiIHk9Ijk1IiBmb250LWZhbWlseT0iQXJpYWwsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMzYiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjOEI4Mzc4IiBsZXR0ZXItc3BhY2luZz0iMyI+CiAgICAgIENPSEFTU0VUCiAgICA8L3RleHQ+CgogICAgPCEtLSBVbmRlcmxpbmVzIGJlbmVhdGggZWFjaCBsZXR0ZXIgb2YgQ09IQVNTRVQgLS0+CiAgICA8bGluZSB4MT0iMTU1IiB5MT0iMTAyIiB4Mj0iMTY3IiB5Mj0iMTAyIiBzdHJva2U9IiM4QjgzNzgiIHN0cm9rZS13aWR0aD0iMSIgLz4KICAgIDxsaW5lIHgxPSIxNzMiIHkxPSIxMDIiIHgyPSIxODUiIHkyPSIxMDIiIHN0cm9rZT0iIzhCODM3OCIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogICAgPGxpbmUgeDE9IjE5MSIgeTE9IjEwMiIgeDI9IjIwMyIgeTI9IjEwMiIgc3Ryb2tlPSIjOEI4Mzc4IiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgICA8bGluZSB4MT0iMjA5IiB5MT0iMTAyIiB4Mj0iMjIxIiB5Mj0iMTAyIiBzdHJva2U9IiM4QjgzNzgiIHN0cm9rZS13aWR0aD0iMSIgLz4KICAgIDxsaW5lIHgxPSIyMjciIHkxPSIxMDIiIHgyPSIyMzkiIHkyPSIxMDIiIHN0cm9rZT0iIzhCODM3OCIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogICAgPGxpbmUgeDE9IjI0NSIgeTE9IjEwMiIgeDI9IjI1NyIgeTI9IjEwMiIgc3Ryb2tlPSIjOEI4Mzc4IiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgICA8bGluZSB4MT0iMjYzIiB5MT0iMTAyIiB4Mj0iMjc1IiB5Mj0iMTAyIiBzdHJva2U9IiM4QjgzNzgiIHN0cm9rZS13aWR0aD0iMSIgLz4KICAgIDxsaW5lIHgxPSIyODEiIHkxPSIxMDIiIHgyPSIyOTMiIHkyPSIxMDIiIHN0cm9rZT0iIzhCODM3OCIgc3Ryb2tlLXdpZHRoPSIxIiAvPgoKICAgIDwhLS0gTGFuZ3VhZ2UgQ2VudGVyIC0tPgogICAgPHRleHQgeD0iMTU1IiB5PSIxMzAiIGZvbnQtZmFtaWx5PSJBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9Im5vcm1hbCIgZmlsbD0iIzhCODM3OCIgbGV0dGVyLXNwYWNpbmc9IjEiPgogICAgICBMYW5ndWFnZSBDZW50ZXIKICAgIDwvdGV4dD4KICAKICWQKICAKPC9zdmc+"
              alt="COHASSET Logo"
              height="45"
              width="auto"
            />
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex items-center gap-8">
            {['inicio', 'cursos', 'nosotros', 'contacto'].map((page) => (
              <button
                key={page}
                onClick={() => setCurrentPage(page)}
                className={`font-semibold transition-all pb-2 ${
                  currentPage === page ? 'border-b-2' : 'hover:opacity-70'
                }`}
                style={{
                  color: currentPage === page ? '#F4A261' : '#636E72',
                  borderColor: currentPage === page ? '#F4A261' : 'transparent',
                }}
              >
                {page.charAt(0).toUpperCase() + page.slice(1)}
              </button>
            ))}
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-2"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            style={{ color: '#2D3436' }}
          >
            {mobileMenuOpen ? (
              <X className="w-6 h-6" />
            ) : (
              <Menu className="w-6 h-6" />
            )}
          </button>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden mt-4 space-y-2 pb-4">
            {['inicio', 'cursos', 'nosotros', 'contacto'].map((page) => (
              <button
                key={page}
                onClick={() => {
                  setCurrentPage(page);
                  setMobileMenuOpen(false);
                }}
                className="block w-full text-left px-4 py-2 rounded-lg font-semibold transition-all"
                style={{
                  background: currentPage === page ? '#FDDBB5' : '#FFF5EB',
                  color: '#2D3436',
                }}
              >
                {page.charAt(0).toUpperCase() + page.slice(1)}
              </button>
            ))}
          </div>
        )}
      </nav>

      {/* Page Content with Smooth Transition */}
      <div className="flex-1 transition-all duration-300 opacity-100 transform">
        {renderPage()}
      </div>

      {/* Footer */}
      <footer
        className="mt-20 px-4 py-12"
        style={{ background: '#2D3436', color: 'white' }}
      >
        <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
          <div>
            <div className="flex items-center gap-2 mb-4">
              <img
                src="data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgNDAwIDIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAKICAGPGRLZNM+CiAgICAgIDwhLS0gR3JhZGllbnQgZm9yIDNEIGVmZmVjdCBvbiBjaXJjbGVzIC0tPgogICAgICA8cmFkaWFsR3JhZGllbnQgaWQ9ImNpcmNsZUdyYWRpZW50IiBjeD0iMzUlIiBjeT0iMzUlIj4KICAgICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdHlsZT0ic3RvcC1jb2xvcjojM0I4MkY2O3N0b3Atb3BhY2l0eToxIiAvPgogICAgICAgIDxzdG9wIG9mZnNldD0iNzAlIiBzdHlsZT0ic3RvcC1jb2xvcjojMjU2M0VCO3N0b3Atb3BhY2l0eToxIiAvPgogICAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3R5bGU9InN0b3AtY29sb3I6IzFFNDBBRjtzdG9wLW9wYWNpdHk6MSIgLz4KICAgICAgPC9yYWRpYWxHcmFkaWVudD4KCiAgICAgIDwhLS0gU2hhZG93IGZpbHRlciBmb3IgY2lyY2xlcyAtLT4KICAgICAgPGZpbHRlciBpZD0iY2lyY2xlU2hhZG93IiB4PSItNTAlIiB5PSItNTAlIiB3aWR0aD0iMjAwJSIgaGVpZ2h0PSIyMDAlIj4KICAgICAgICA8ZmVEcm9wU2hhZG93IGR4PSIyIiBkeT0iMiIgc3RkRGV2aWF0aW9uPSIxLjUiIGZsb29kLW9wYWNpdHk9IjAuMyIgLz4KICAgICAgPC9maWx0ZXI+CiAgPC9kZWZzPgoKICA8IS0tIFN1bmJ1cnN0IGNpcmNsZSBwYXR0ZXJuIG9uIHRoZSBsZWZ0IC0tPgogIDxnIGlkPSJzdW5idXJzdCI+CiAgICAgIDwhLS0gQ2VudGVyIHBvaW50IGF0IGFwcHJveGltYXRlbHkgeD04MCwgeT0xMDAgLS0+CgogICAgICA8IS0tIFJpZ2h0IHJheSAoMCBkZWdyZWVzKSAtLT4KICAgICAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMiIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgogICAgICA8Y2lyY2xlIGN4PSIxMTUiIGN5PSIxMDAiIHI9IjkiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iMTI4IiBjeT0iMTAwIiByPSI2IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CgogICAgICA8IS0tIFRvcC1yaWdodCByYXkgKDQ1IGRlZ3JlZXMpIC0tPgogICAgICA8Y2lyY2xlIGN4PSI5NS40IiBjeT0iNzkuNiIgcj0iMTEiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iMTA2LjYiIGN5PSI2OC40IiByPSI4IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjExNi41IiBjeT0iNTcuNSIgcj0iNSIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgoKICAgICAgPCEtLSBUb3AgcmF5ICg5MCBkZWdyZWVzKSAtLT4KICAgICAgPGNpcmNsZSBjeD0iODAiIGN5PSI3OCIgcj0iMTEuNSIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgogICAgICA8Y2lyY2xlIGN4PSI4MCIgY3k9IjYzIiByPSI4LjUiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iODAiIGN5PSI1MCIgcj0iNS41IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CgogICAgICA8IS0tIFRvcC1sZWZ0IHJheSAoMTM1IGRlZ3JlZXMpIC0tPgogICAgICA8Y2lyY2xlIGN4PSI2NC42IiBjeT0iNzkuNiIgcj0iMTEiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iNTMuNCIgY3k9IjY4LjQiIHI9IjgiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iNDMuNSIgY3k9IjU3LjUiIHI9IjUiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KCiAgICAgIDwhLS0gTGVmdCByYXkgKDE4MCBkZWdyZWVzKSAtLT4KICAgICAgPGNpcmNsZSBjeD0iNjAiIGN5PSIxMDAiIHI9IjEyIiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjQ1IiBjeT0iMTAwIiByPSI5IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjMyIiBjeT0iMTAwIiByPSI2IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CgogICAgICA8IS0tIEJvdHRvbS1sZWZ0IHJheSAoMjI1IGRlZ3JlZXMpIC0tPgogICAgICA8Y2lyY2xlIGN4PSI2NC42IiBjeT0iMTIwLjQiIHI9IjExIiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjUzLjQiIGN5PSIxMzEuNiIgcj0iOCIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgogICAgICA8Y2lyY2xlIGN4PSI0My41IiBjeT0iMTQyLjUiIHI9IjUiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KCiAgICAgIDwhLS0gQm90dG9tIHJheSAoMjcwIGRlZ3JlZXMpIC0tPgogICAgICA8Y2lyY2xlIGN4PSI4MCIgY3k9IjEyMiIgcj0iMTEuNSIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgogICAgICA8Y2lyY2xlIGN4PSI4MCIgY3k9IjEzNyIgcj0iOC41IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjgwIiBjeT0iMTUwIiByPSI1LjUiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KCiAgICAgIDwhLS0gQm90dG9tLXJpZ2h0IHJheSAoMzE1IGRlZ3JlZXMpIC0tPgogICAgICA8Y2lyY2xlIGN4PSI5NS40IiBjeT0iMTIwLjQiIHI9IjExIiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjEwNi42IiBjeT0iMTMxLjYiIHI9IjgiIGZpbGw9InVybCgjY2lyY2xlR3JhZGllbnQpIiBmaWx0ZXI9InVybCgjY2lyY2xlU2hhZG93KSIgLz4KICAgICAgPGNpcmNsZSBjeD0iMTE2LjUiIGN5PSIxNDIuNSIgcj0iNSIgZmlsbD0idXJsKCNjaXJjbGVHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNjaXJjbGVTaGFkb3cpIiAvPgoKICAgICAgPCEtLSBMYXJnZSBjZW50cmFsIGNpcmNsZSAtLT4KICAgICAgPGNpcmNsZSBjeD0iODAiIGN5PSIxMDAiIHI9IjE0IiBmaWxsPSJ1cmwoI2NpcmNsZUdyYWRpZW50KSIgZmlsdGVyPSJ1cmwoI2NpcmNsZVNoYWRvdykiIC8+CiAgPC9nPgogIAogIDwhLS0gVGV4dCBvbiB0aGUgcmlnaHQgLS0+CiAgPGcgaWQ9InRleHQiPgogICAgPCEtLSBDT0hBU1NFVCB3aXRoIHVuZGVybGluZXMgLS0+CiAgICA8dGV4dCB4PSIxNTUiIHk9Ijk1IiBmb250LWZhbWlseT0iQXJpYWwsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMzYiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjOEI4Mzc4IiBsZXR0ZXItc3BhY2luZz0iMyI+CiAgICAgIENPSEFTU0VUCiAgICA8L3RleHQ+CgogICAgPCEtLSBVbmRlcmxpbmVzIGJlbmVhdGggZWFjaCBsZXR0ZXIgb2YgQ09IQVNTRVQgLS0+CiAgICA8bGluZSB4MT0iMTU1IiB5MT0iMTAyIiB4Mj0iMTY3IiB5Mj0iMTAyIiBzdHJva2U9IiM4QjgzNzgiIHN0cm9rZS13aWR0aD0iMSIgLz4KICAgIDxsaW5lIHgxPSIxNzMiIHkxPSIxMDIiIHgyPSIxODUiIHkyPSIxMDIiIHN0cm9rZT0iIzhCODM3OCIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogICAgPGxpbmUgeDE9IjE5MSIgeTE9IjEwMiIgeDI9IjIwMyIgeTI9IjEwMiIgc3Ryb2tlPSIjOEI4Mzc4IiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgICA8bGluZSB4MT0iMjA5IiB5MT0iMTAyIiB4Mj0iMjIxIiB5Mj0iMTAyIiBzdHJva2U9IiM4QjgzNzgiIHN0cm9rZS13aWR0aD0iMSIgLz4KICAgIDxsaW5lIHgxPSIyMjciIHkxPSIxMDIiIHgyPSIyMzkiIHkyPSIxMDIiIHN0cm9rZT0iIzhCODM3OCIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogICAgPGxpbmUgeDE9IjI0NSIgeTE9IjEwMiIgeDI9IjI1NyIgeTI9IjEwMiIgc3Ryb2tlPSIjOEI4Mzc4IiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgICA8bGluZSB4MT0iMjYzIiB5MT0iMTAyIiB4Mj0iMjc1IiB5Mj0iMTAyIiBzdHJva2U9IiM4QjgzNzgiIHN0cm9rZS13aWR0aD0iMSIgLz4KICAgIDxsaW5lIHgxPSIyODEiIHkxPSIxMDIiIHgyPSIyOTMiIHkyPSIxMDIiIHN0cm9rZT0iIzhCODM3OCIgc3Ryb2tlLXdpZHRoPSIxIiAvPgoKICAgIDwhLS0gTGFuZ3VhZ2UgQ2VudGVyIC0tPgogICAgPHRleHQgeD0iMTU1IiB5PSIxMzAiIGZvbnQtZmFtaWx5PSJBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9Im5vcm1hbCIgZmlsbD0iIzhCODM3OCIgbGV0dGVyLXNwYWNpbmc9IjEiPgogICAgICBMYW5ndWFnZSBDZW50ZXIKICAgIDwvdGV4dD4KICAKICWQKICAKPC9zdmc+"
                alt="COHASSET Logo"
                height="40"
                width="auto"
              />
              <h3 className="font-bold" style={{ color: '#F4A261' }}>
                COHASSET
              </h3>
            </div>
            <p className="text-sm" style={{ color: '#B5C9B3' }}>
              Academia de inglés con metodología innovadora y profesores certificados.
            </p>
          </div>
          <div>
            <h4 className="font-semibold mb-4">Enlaces Rápidos</h4>
            <ul className="space-y-2 text-sm" style={{ color: '#B5C9B3' }}>
              <li><a href="#" className="hover:text-white transition-all">Cursos</a></li>
              <li><a href="#" className="hover:text-white transition-all">Nosotros</a></li>
              <li><a href="#" className="hover:text-white transition-all">Contacto</a></li>
            </ul>
          </div>
          <div>
            <h4 className="font-semibold mb-4">Contacto</h4>
            <p className="text-sm" style={{ color: '#B5C9B3' }}>Email: info@cohassetchr.com</p>
            <p className="text-sm" style={{ color: '#B5C9B3' }}>Tel: +51 1 2345678</p>
          </div>
        </div>
        <div
          className="border-t pt-8 text-center text-sm"
          style={{ borderColor: '#636E72', color: '#B5C9B3' }}
        >
          <p>&copy; 2024 COHASSET Language Center. Todos los derechos reservados.</p>
        </div>
      </footer>

      {/* WhatsApp Floating Button */}
      <a
        href="https://wa.me/51"
        target="_blank"
        rel="noopener noreferrer"
        className="fixed bottom-6 right-6 p-4 rounded-full shadow-lg transition-all hover:scale-110 active:scale-95 z-40"
        style={{ background: '#8BA888' }}
      >
        <MessageCircle className="w-6 h-6 text-white" />
      </a>
    </div>
  );
}
