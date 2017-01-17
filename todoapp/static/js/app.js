
var socket = io();

var todovm = new Vue({
  el: "#todoapp",
  data: {
    searchfield: '',
    nexthref: '',
    todotext: '',
    todos1: [],
    busy: false,
  },

  watch: {
    searchfield: function (searchexpr) {
      this.search(searchexpr);
    }
  },
  
  methods: {
    
    search: function (searchexpr) {

      var vm = this;
      if (searchexpr == '') {
	init();
	return ;
      }
      axios("/api/v1/todos?where={\"todotext\": { \"$regex\": \"" +  searchexpr + "\"}}")
	.then(function (response){
	  vm.todos1 = response.data._items;
	  if (response.data._links.next) {
	    vm.nexthref = response.data._links.next.href;
	  } else {
	    vm.nexthref = false;
	  }
	});
    },
    
    loadMore: function() {
      var vm = this;
      if (vm.nexthref) {
	vm.busy = true;
	setTimeout(() => {
	  if (vm.nexthref) {
	    axios('/api/v1/' + vm.nexthref)
	      .then (function (response) {
		vm.todos1 = vm.todos1.concat(response.data._items);
		if (response.data._links.next) {
		  vm.nexthref = response.data._links.next.href;
		} else {
		  vm.nexthref = false;
		}
	      });
	  }
	  vm.busy = false;
	}, 1000);
      }
    },
    // send to api
    send: function (event) {
      vm = this;
      axios.post('/api/v1/todos',
		 {
		   todotext: this.todotext
		 }, {
		   headers: { 
		     "Content-Type": "application/json"
		   }})
	.then (function (response) {
	  axios('/api/v1/' + response.data._links.self.href)
	    .then(function (response) {
	      socket.emit('newtodo', response.data);
	      vm.todos1.splice(0, 0, response.data);
	    });
	})
	.catch(function (error) {
	  console.log(error);
	});
    },
    
    removeit: function (todoobject, index) {
      vm = this
      axios.delete(
	'/api/v1/' + todoobject._links.self.href, {
	  headers: {
	    "If-Match": todoobject._etag
	  }
	}
      )
	.then(function () {
	  socket.emit('removetodo', index);
	  vm.todos1.splice(
	    index,
	    1
	  );
	});
    },

    toggledone: function (todoobject, index) {
      vm = this;
      axios.patch(
	'/api/v1/' + todoobject._links.self.href,
	{
	  done: !todoobject.done
	},
	{
	  headers: {
	    "If-Match": todoobject._etag,
	    "Content-Type": "application/json"
	  }
	}
      )
	.then(function (response) {
	  axios('/api/v1/' + response.data._links.self.href)
	    .then(function (response) {
	      socket.emit('donetodo', {
		index: index,
		data: response.data
	      });
	      vm.$set(todovm.todos1, index, response.data);
	    });

	});
    },


  }
});

Vue.component('todoitem', {
  template: `
     	    <div class="todo">
		<p> {{ todo.todotext }}</p>
		<button class="delete" v-on:click="$emit('removeit')">
		    <i class="fa fa-trash-o" aria-hidden="true"></i>
		</button>
		<button v-bind:class="getstate" v-on:click="$emit('doneundone')">
		    <i class="fa fa-check" aria-hidden="true"></i>
		</button>
	    </div>`,
  props: ['todo'],

  computed : {
    getstate: function () {
      return (this.todo.done ? 'notdone' : 'done');
    }
  }
});

function init() {
  axios('/api/v1/todos?sort=-_created')
    .then (function (response) {
      
      todovm.todos1 = response.data._items;
      if (response.data._links.next) {
	todovm.nexthref = response.data._links.next.href;
      } else {
	todovm.nexthref = false;
      }
    });
}

init();

socket.on('newtodo', function(data) {
  $.notify("Someone added a todo.", "info");
  todovm.todos1.splice(0, 0, data);
});

socket.on('removetodo', function(data) {
  if (todovm.todos1[data]) {
    $.notify("Someone removed a todo.", "info");
    todovm.todos1.splice(
      data,
      1
    );
  }
}) ;


socket.on('donetodo', function (data) {
  if (todovm.todos1[data.index]) {
    $.notify("Someone has changed the state of a todo.", "info");
    todovm.$set(todovm.todos1, data.index, data.data);
  }
});
