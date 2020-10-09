
// Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        count: 0,
        instrument: {},
    },
    mutations: {
        increment(state) {
            state.count++
        },
        changeInstrument(state, payload) {
            state.instrument = payload
        }
    },
    getters: {
        instrumentId: state => {
            return state.instrument.id;
        },
        instrumentLocation: state => {
            return state.instrument.location;
        },
        instrumentName: state => {
            return state.instrument.Name;
        }
    },
})
Vue.component("instrument", {
    template: "#instrument-template",
    delimiters: ["<%", "%>"],
    store: store,
    props: {
        item: Object
    },
    data: function () {
        return {
            instrumentSelected: {},
            isOpen: false,
            level: 'grey',
            commentId: null,
        };
    },
    computed: {
        hasReply: function () {
            return this.item.children && this.item.children.length;
        }
    },
    methods: {
        holder: function () {
            return 'nice';
        }
    }
});

mainApp = new Vue({
    el: '#mainApp',
    delimiters: ["<%", "%>"],
    vuetify: new Vuetify(),
    store: store,
    props: {
        source: String,
    },
    data: () => ({
        treeData: {},
        drawer: false,
        instrumentList: null,
        instrumentDialog: false,
        detailDialog: false,
        selectedInstrument: Object,
        selectedIndex: null,
        showInstruments: false,
        gyroData: Object,
        selectedCategory: '',
        formattedCategory: 'All Instruments',
        instrumentCategories: [
            'gyro',
            'motion',
            'position',
            'temperature',
            'barometric'
        ],
        colorList: [{
            color:
                "blue lighten-3",
        }, {
            color:
                "red lighten-3",
        }, {
            color:
                "green lighten-3",
        }, {
            color:
                "yellow lighten-3",
        }, {
            color:
                "blue-grey lighten-3",
        }, {
            color:
                "deep-orange lighten-3",
        },
        ],
    }),
    methods: {
        getGyroData: function() {
            const url = "/api/gyrodata/?instrument=" + this.selectedInstrument.id;
            return axios
                .get(url)
                .then(response => {
                    this.showInstruments = true;
                    return response.data
                })
                .catch(error => {
                    console.log(error)
                })
                .finally(() => this.loading = false);
        },
        loadGyroData: async function () {
            this.gyroData = await this.getGyroData();
            console.log('test555')
        },
        getJson: function () {
            const url = "/api/instruments/?category=" + this.selectedCategory;
            return axios
                .get(url)
                .then(response => {
                    this.showInstruments = true;
                    return response.data
                })
                .catch(error => {
                    console.log(error)
                })
                .finally(() => this.loading = false);
        },
        loadJson: async function () {
            this.showInstruments = false;
            this.instrumentList = await this.getJson();
        },
        saveInstrument: async function (key) {
            const saveResult = await this.saveInstrumentPromise(key);
            if (saveResult) {
                this.instrumentList[this.selectedIndex] = this.selectedInstrument;
                this.instrumentDialog = false;
            }
            else {
                console.log('ERROR')
            }
        },
        selectCategory: function (category) {
            this.selectedCategory = category;
            this.formattedCategory = this.getFormattedCategory(category);
            this.loadJson();
        },
        saveInstrumentPromise: function (key) {
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            const url = '/api/instruments/' + key + '/'
            return axios.put(url, this.selectedInstrument)
                .then(function (response) {
                    console.log(response);
                    return response.data;
                })
                .catch(function (error) {
                    console.log(error);
                    return false;
                })
        },
        storeID: function (id) {

        },
        viewInstrument: function (index) {
            this.selectedInstrument = this.instrumentList[index];
            this.loadGyroData()
        },
        getCardColor: function (index) {
            const colors = this.colorList;
            category = this.instrumentList[index].category
            switch (category) {
                case 'gyro':
                    return colors[0].color;
                case 'position':
                    return colors[2].color;
                case 'temperature':
                    return colors[5].color;
                case 'barometric':
                    return colors[3].color;
                case 'motion':
                    return colors[4].color;
            }
        },
        getFormattedCategory: function(category) {
            switch (category) {
                case 'gyro':
                    return 'Gyro';
                case 'position':
                    return 'Position';
                case 'temperature':
                    return 'Temperature';
                case 'barometric':
                    return 'Barometric';
                case 'motion':
                    return 'Motion';
                case '':
                    return 'All Instruments';
                case '&starred=true':
                    return 'Starred';
            }
        },
        getStarred: function (index) {
            if (this.instrumentList[index].starred) {
                return 'yellow';
            }
            else {
                return "grey darken-2";
            }
        },
        toggleStarred: function (index) {
            let instrument = this.instrumentList[index];
            instrument.starred = !instrument.starred;
            this.selectedInstrument = instrument;
            this.selectedIndex = index;
            this.saveInstrument(instrument.id);
        },
        selectInstrument: function (index) {
            // assign a shallow copy
            let instrument = Object.assign({}, this.instrumentList[index]);
            this.selectedInstrument = instrument;
            this.selectedIndex = index;
        }
    }
})

